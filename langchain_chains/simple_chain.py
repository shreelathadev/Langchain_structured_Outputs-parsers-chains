from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite', max_output_tokens = 256)

prompt=PromptTemplate(
    template = "generate 5 imp facts about {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser 

res = chain.invoke({'topic':'India'})

print(res)

chain.get_graph().print_ascii()

