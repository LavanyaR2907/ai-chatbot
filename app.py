import streamlit as st
import os
os.environ['GOOGLE_API_KEY']=st.secrects['GOOGLE_API_KEY']
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Set Google API Key from Streamlit secrets
os.environ['GOOGLE_API_KEY'] = st.secrets["GOOGLE_API_KEY"]

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Initialize chat history if not already done
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        SystemMessage(content="You are a helpful assistant.")
    ]

# Streamlit app title
st.title("🤖 Gemini 2 Chatbot")

# Display previous chat messages
for msg in st.session_state.chat_history:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.markdown(msg.content)

# Chat input box
user_input = st.chat_input("Say something...")

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = llm.invoke(st.session_state.chat_history)

    # Add AI response to chat history
    st.session_state.chat_history.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(response.content)
