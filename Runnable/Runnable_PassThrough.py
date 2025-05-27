from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough


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
joke_gen_chain=RunnableSequence(
    prompt1,model,parser
)
parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "explain":RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)
# Run the chain with a specific input
result = final_chain.invoke({"topic": "cricket"})
print("Here is the Joke",result["joke"])  # Output: A joke about cats   
print("----------------------------------------------")
print("Here is the Explanation",result["explain"])  # Output: A joke about cats