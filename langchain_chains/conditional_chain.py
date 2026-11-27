from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv(find_dotenv())

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash-lite')

class feedback(BaseModel):
    sentiment : Literal['Positive','Negative'] = Field(description='Give the sentiment of the feedback')

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback into positive or negative. \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Give appropriate response for the postive feedback, {feedback}',
    input_variables= ['feedback']
)

prompt3 = PromptTemplate(
    template='Give approriate response for this negative feedback, {feedback}',
    input_variables=['feedback']
)

# branch_chain = RunnableBranch(
#     (condition1, chain1),
#     (condition2, chain2),
#     default_chain
# )

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'Negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find a sentiment")
)

chain = classifier_chain | branch_chain

res = chain.invoke({'feedback':'This is a wonderful phone'})

print(res)

chain.get_graph().print_ascii()