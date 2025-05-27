from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()
print("Welcome to the chatbot! Type 'exit' to end the conversation.")
prompt1 = PromptTemplate(
    template="write a tweet about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()

prompt2= PromptTemplate(
    template="write a linked post about {topic}",
    input_variables=["topic"]
)

parrale_chain=RunnableParallel({
    "tweet":RunnableSequence(prompt1,model,parser),
    "linked":RunnableSequence(prompt2,model,parser)
})
# Run the chain with a specific input
result = parrale_chain.invoke({"topic": "AI"})
print("Here is the Tweet",result["tweet"])  # Output: A tweet about AI
print("----------------------------------------------")
print("Here is the Linked Post",result["linked"])  # Output: A LinkedIn post about AI 
# Output: A joke about cats

