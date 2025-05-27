from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableBranch


load_dotenv()
print("Welcome to the Runnable Lambda.")
def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template="Detail about the  {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the  {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()
detail_chain=RunnableSequence(
    prompt2,model,parser
)

branch_chain=RunnableBranch(
     (lambda x: len(x.split()) >200,RunnableSequence(prompt2,model,parser)),
     RunnablePassthrough()
)
final_chain=RunnableSequence(
    detail_chain,
    branch_chain
)
# Run the chain with a specific input
result = final_chain.invoke({"topic": "cricket"})
print("Here is the Detail",result)  # Output: A joke about cats

