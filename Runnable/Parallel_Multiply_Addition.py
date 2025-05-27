from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel

load_dotenv()
print("Welcome to the chatbot! Type 'exit' to end the conversation.")
prompt1 = PromptTemplate(
    template="Multiply  {number1} and {number2}",
    input_variables=["number1","number2"]
   )

model = ChatOpenAI()
parser = StrOutputParser()

prompt2= PromptTemplate(
    template="Add {number1} and {number2}", 
    input_variables=["number1","number2"]
)

prompt3= PromptTemplate(
    template="Substract {number1} and {number2}",
    input_variables=["number1","number2"]
)

parrale_chain=RunnableParallel({
    "multiply":RunnableSequence(prompt1,model,parser),
    "add":RunnableSequence(prompt2,model,parser),
    "substract":RunnableSequence(prompt3,model,parser)
})

# Run the chain with a specific input
result = parrale_chain.invoke({"number1": 5,"number2": 10})
print("Here is the Multiplication",result["multiply"])  # Output: A multiplication of 5 and 10
print("----------------------------------------------")
print("Here is the Addition",result["add"])  # Output: A addition of 5 and 10
print("----------------------------------------------")
print("Here is the Substraction",result["substract"])  # Output: A substraction of 5 and 10
