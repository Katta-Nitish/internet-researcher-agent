from langchain_community.vectorstores import Chroma
from tavily import TavilyClient
import streamlit as st
from langchain.agents import create_agent
from langchain.messages import HumanMessage
from langchain_huggingface import HuggingFaceEmbeddings
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List, TypedDict
from langgraph.graph import StateGraph, START,END
thread_config = {"configurable": {"thread_id": "Session_1"}}
class State(TypedDict):
    query: str
    web_result: List[dict]
    embedding : str
    final: str
@st.cache_resource
def image():
    return st.image("D:\\The_Internet_Researcher\\i1.png", width=200)
st.title("The Internet Researcher")
image()
if "agent_memory" not in st.session_state:
    st.session_state.agent_memory=InMemorySaver()
if "report" not in st.session_state:
    st.session_state.report=None
with st.sidebar:
    st.title("⚙️ Configuration")
    user_key = st.text_input("Enter Gemini API Key", type="password")
    st.caption("Get your free Gemini API key [here](https://aistudio.google.com/app/apikey).")
if user_key:
    def web_search(state: State):
        tavil = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])
        response=tavil.search(state['query'])
        return {'web_result': response['results']}

    def embed(state: State):
        model_name = "BAAI/bge-small-en-v1.5"
        model_kwargs = {'device': 'cpu'}
        encode_kwargs = {'normalize_embeddings': True}
        
        embedding = HuggingFaceEmbeddings(
            model_name=model_name,
            model_kwargs=model_kwargs,
            encode_kwargs=encode_kwargs
        )
        texts = [res['content'] for res in state['web_result']]
        metadatas = [{"source": res['url']} for res in state['web_result']]
        vectorstore = Chroma.from_texts(texts, embedding, metadatas=metadatas)
        relevant_docs = vectorstore.similarity_search(state['query'], k=5)
        formatted_report_input = ""
        for doc in relevant_docs:
            source_url = doc.metadata.get("source", "Unknown Source")
            formatted_report_input += f"CONTENT: {doc.page_content}\nSOURCE URL: {source_url}\n\n"
        return {"embedding": formatted_report_input}

    def final_output(state: State):
        llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=user_key, temperature=0.2)
        prompt = (
            f"RESEARCH DATA:\n{state['embedding']}\n\n"
            f"TASK: Draft a comprehensive report on: {state['query']}.\n\n"
            f"INSTRUCTIONS:\n"
            f"1. Use the Research Data provided to write the report.\n"
            f"2. At the very end of the report, add a section titled '--- SOURCES ---' and list all unique URLs used.\n"
            f"3. After the sources, add a final line: 'Report Generated on: {current_date}'."
        )
        response=llm.invoke(prompt)
        return {'final': response.content}


    @st.cache_resource
    def get_graph():
        builder=StateGraph(State)
        builder.add_node("search",web_search)
        builder.add_node("embed",embed)
        builder.add_node("final",final_output)

        builder.add_edge(START,"search")
        builder.add_edge('search','embed')
        builder.add_edge('embed','final')
        builder.add_edge('final',END)
        return builder.compile(checkpointer=st.session_state.agent_memory)
    research=get_graph()

    user_input=st.text_input("Enter your research topic")
    if st.button("Start Research💡"):
        initial_messagge={"query":user_input}
        with st.status("Researcher is running...", expanded=True) as status:
            for event in research.stream(initial_messagge, config=thread_config):
                for node_name, state_update in event.items():
                    st.write(f"✅ Completed: {node_name}")
                status.update(label="Research Finished!", state="complete")
        final_state=research.get_state(config=thread_config).values
        st.session_state.report = final_state["final"]
    if st.session_state.report:
        st.markdown("### 📑 Final Report")
        # --- SIDEBAR: GRAPH MEMORY ---
        with st.sidebar:
        # Optional: Move your logo/image here to make it look like a dashboard
        # image() 
        
            st.header("🧠 Graph Memory")
        
            if st.session_state.report:
                with st.expander("📄 View Raw Research Data", expanded=False):
                    st.info("This is the exact text the agent is reading to answer your questions.")
                    st.text_area(
                        label="Full Context", 
                        value=st.session_state.report, 
                        height=400
                    )
            else:
                st.write("No research data in memory. Start a search to populate.")
        st.write(st.session_state.report)

    agent=create_agent(
        model=ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=user_key, temperature=0.2),
        checkpointer=st.session_state.agent_memory,
        system_prompt=f'''You are an Expert Research Assistant. 

    ### YOUR DATA SOURCE:
    {st.session_state.report if st.session_state.report else "No report available yet"}

    ### YOUR INSTRUCTIONS:
    1. Always check the 'DATA SOURCE' above before answering. 
    2. If the user's question relates to the data source, prioritize that information over your general knowledge.
    3. If the user asks about abbreviations (like SoH), look for their meaning within the context of the provided report.
    4. If the question is unrelated to the report, provide a helpful general response.
    5. If the report is empty, respond with "I don't have any information yet. Please start a research to populate my data source."''',
        )
    if st.session_state.report:
        if "messages" not in st.session_state:
            st.session_state.messages=[]
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message['content'])
        if prompt:=st.chat_input("user"):
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role":"user","content":prompt})
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    response=agent.invoke(
                        {"messages":[HumanMessage(content=prompt)]},
                        config=thread_config,
                        )
                final_content = response["messages"][-1].content
                st.markdown(final_content)
                st.session_state.messages.append({"role":"assistant","content":final_content})

else:
    st.warning("Please provide the Google API KEY")