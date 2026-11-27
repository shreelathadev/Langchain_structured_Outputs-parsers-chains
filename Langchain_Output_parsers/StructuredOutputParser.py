from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv, find_dotenv
from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
from langchain_classic.output_parsers.structured import StructuredOutputParser, ResponseSchema 

load_dotenv(find_dotenv())

# llm = HuggingFaceEndpoint(repo_id="mistralai/Mistral-7B-Instruct-v0.2", task='text-generation')
# model = ChatHuggingFace(llm=llm)

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

schema = [
    ResponseSchema(name='fact_1', description= 'fact_1 about the topic'),
    ResponseSchema(name='fact_2', description= 'fact_2 about the topic'),
    ResponseSchema(name='fact_3', description= 'fact_3 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="Give 3 facts about {topic}, \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'black hole'})
# res = model.invoke(prompt)
# result = parser.parse(res.content[0]['text'])
# print(result)

#or invoke using chain
chain = template | model | parser 
res=chain.invoke({'topic':'black hole'})
print(res)
