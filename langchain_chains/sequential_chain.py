from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite', max_output_tokens = 256)

prompt1 = PromptTemplate(
    template = "generate a detailed report on {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template = " generate a 5 point summary on the given {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser
res = chain.invoke({'topic':'Unemployment in India'})
print(res)

chain.get_graph().print_ascii()