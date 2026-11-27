
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate 

load_dotenv(find_dotenv())

# llm = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v0.6", task="text-generation") or google/gemma-2-2b-it
# chat_model = ChatHuggingFace(llm=llm)

chat_model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

# 1st prompt -> detailed prompt
template1 = PromptTemplate(
    template=" Write a detailed report on.{topic}",
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='write a 5 line summary on the given text.\n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic':'black hole'})
text = chat_model.invoke(prompt1)

prompt2 = template2.invoke({'text': text})
result = chat_model.invoke(prompt2)

print(result.content)