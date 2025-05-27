from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(model="gpt-4")

# List to store chat history as HumanMessage and AIMessage
chat_history = []

print("Welcome to the chatbot! Type 'exit' to end the conversation.")

while True:
    # Take user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    
    # Add the user input as a HumanMessage to the chat history
    chat_history.append(HumanMessage(content=user_input))
    
    # Get response from the model
    response = chat_model.invoke(chat_history)
    
    # Add the AI response as an AIMessage to the chat history
    chat_history.append(AIMessage(content=response.content))
    
    # Print the response
    print(f"Chatbot: {response.content}")

# Optional: Print the chat history at the end
print("\nChat History:")
for message in chat_history:
    if isinstance(message, HumanMessage):
        print(f"You: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"Chatbot: {message.content}")