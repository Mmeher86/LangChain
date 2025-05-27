from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda


load_dotenv()
print("Welcome to the Runnable Lambda.")
def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template="write a joke about {topic}",
    input_variables=["topic"]
)

model = ChatOpenAI()
parser = StrOutputParser()
joke_gen_chain=RunnableSequence(
    prompt,model,parser
)

parallel_chain=RunnableParallel({
    "joke":RunnablePassthrough(),
    "count":RunnableLambda(word_count)
})
final_chain=RunnableSequence(
    joke_gen_chain,
    parallel_chain
)
# Run the chain with a specific input
result = final_chain.invoke({"topic": "cricket"})
print("Here is the Joke",result['joke'])  # Output: A joke about cats
print("----------------------------------------------")
print("Here is the Count",result['count'])  # Output: A joke about cats

