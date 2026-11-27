from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name:str = 'nitish'
    age: Optional[int] = None
    email : EmailStr 
    cgpa : float = Field(gt=0, lt=10, description='enter your cgpa i decimal value from 1 to 10', default=5)

new_student = {'name':'sri', 'age': '36', 'email': 'abc@gmail.com', 'cgpa':9.9}

student = Student(**new_student)

student_dict = student.model_dump()  # we are here just converting this to dict format. or u can also do 'dict(student)'
print(student_dict)

student_json = student.model_dump_json()
print(student_json)