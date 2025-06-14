from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence

load_dotenv()
print("Welcome to the chatbot! Type 'exit' to end the conversation.")
prompt1 = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

prompt2= PromptTemplate(
    template="Explain the joke in innovative way {text}",
    input_variables=["text"]
)

chain=RunnableSequence(
    prompt1,model,parser,prompt2,model,parser
)
# Run the chain with a specific input
result = chain.invoke({"topic": "horses"})
print(result)
# Output: A joke about cats

