from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite',max_output_tokens = 256, temperature = 0.8)

class person(BaseModel):
    name : str = Field(description="name of the person"),
    age : int = Field(gt=18, description="age of the person"),
    city : str = Field(description="city the person resides in")

parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(
    template="generate the name, age and city of a {place} person, {format_instruction} ",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

# prompt = template.invoke({'place':'Indian'})
# res = model.invoke(prompt)
# fin_res = parser.parse(res.content[0]['text'])
# print(fin_res)

# OR

chain = template | model | parser 
res=chain.invoke({'place':"Indian"})
print(res) 