from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite', max_output_tokens = 256)

# 1st prompt -> detailed prompt
template1 = PromptTemplate(
    template=" Write a detailed report on.{topic}",
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='write a 5 point summary on the given text.\n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser 

result = chain.invoke({'topic':'black hole'})

print(result)