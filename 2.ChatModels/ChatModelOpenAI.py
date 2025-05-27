from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4")
input_text = input("Ask your question: ")
result=model.invoke(input_text)
print(result.content)  # Test the model with a simple prompt