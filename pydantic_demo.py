from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'Akshay'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, default= 6, descreption="A decimal value represent the cgpa of the student")

new_student = {'age':22, 'email':'abs@gmail.com'} #'cgpa':5.2}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()