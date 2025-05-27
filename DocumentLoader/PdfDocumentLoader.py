from langchain_community.document_loaders import DirectoryLoader,PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()
print("Welcome to the PDF Document Loader.")

loader=DirectoryLoader(
    path="Docs",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)
documents=loader.lazy_load()
#print(len(documents))

prompt = PromptTemplate(
    template="Can you please get the profile for Mortgage Banking from \n {files}",
    input_variables=["files"]
)
model = ChatOpenAI()
parser = StrOutputParser()   
chain=prompt| model | parser
count=0
for doc in documents:
    print("Here is the Document link",doc.metadata['source'])
    print(chain.invoke({"files": doc.page_content})) 
    count+=1

print("Total number of documents processed:",count)

