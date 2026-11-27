from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite',max_output_tokens = 256, temperature = 0.8)

# create the JSON parser
parser = JsonOutputParser()

# create prompt template
template = PromptTemplate(
    template='give me the name, age and city of a fictional person. \n {format_instruction}',
    input_variables=[],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)


# # in the below line we can use template.invoke() or template.format(), both are same just their outpit differ, one format returns str and invoke returs promptvalue. both format the template but thier return values are diff.
# prompt = template.format()
# result = model.invoke(prompt) #now gemini recieves the formatted prompt.
# final_res = parser.parse(result.content[0]["text"]) # This is where the actual parsing happens. The parser takes the LLM's JSON-formatted response and converts it into a Python dictionary.


# another way of invoking is by using chain method
chain = template | model | parser 
res = chain.invoke({})
print(res)

# print(result)
# print(final_res)
# print(type(final_res))
