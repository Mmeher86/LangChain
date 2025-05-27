import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(model="gpt-4")

# Streamlit app title
st.title("Chatbot with LangChain")

# Initialize chat history in session state
chat_history = []

# Input box for user input
user_input = st.text_input("You:", key="user_input")

# Process user input
if st.button("Send"):
    if user_input:
        # Add user input as a HumanMessage to the chat history
        chat_history.append(HumanMessage(content=user_input))
        
        # Get response from the model
        response = chat_model.invoke(chat_history)
        
        # Add AI response as an AIMessage to the chat history
        chat_history.append(AIMessage(content=response.content))
        
        # Clear the input box
        
        
        st.write(f"**AI:** {response.content}")
# Display chat history 
# runthis file with streamlit run Chatbot_LangChain_UI.py command in terminal
st.subheader("Chat History")
