from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the ChatOpenAI model
chat_model = ChatOpenAI(model="gpt-4")

# List to store chat historyw
chat_history = []

print("Welcome to the chatbot! Type 'exit' to end the conversation.")

while True:
    # Take user input
    user_input = input("You: ")
    
    # Exit condition
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    chat_history.append(user_input)
    # Get response from the model
    response = chat_model.invoke(chat_history)
    
    # Store the question and response in chat history
    chat_history.append( response.content)
    
    # Print the response
    print(f"Chatbot: {response.content}")

# Optional: Print the chat history at the end
print("\nChat History:")
print("\n".join(chat_history))