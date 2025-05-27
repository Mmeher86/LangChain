from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
prompt = PromptTemplate(
    template="Can you please count how many could is there from \n {text}",
    input_variables=["text"]
)
model = ChatOpenAI()
parser = StrOutputParser()

loader=TextLoader("Learning Tree.txt")
documents=loader.load()

chain=prompt| model | parser
#print( documents[0].page_content)
print(chain.invoke({"text": documents[0].page_content}))
# Output:
#clsprint("Here is the Document link",result)  # Output: A joke about cats
# print(type(documents))