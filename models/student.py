# import statement
from pydantic import BaseModel

class Student(BaseModel):
    student_name: str
    student_mail: str
    student_phone: str
    