from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
print(llm.invoke("What is the capital of France?"))  # Should return "Paris"
input_text =input("Ask your question: ")
response = llm.invoke(input_text)  # Should return "Paris"
print(f"Response: {response}")  # Print the response from the LLM
