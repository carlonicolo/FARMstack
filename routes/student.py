# import statements
from fastapi import APIRouter
from models.student import Student
from config.database import connection
from schemas.student import studentEntity, listOfStudentEntity
from bson import ObjectId

student_router = APIRouter()

@student_router.get('/hello')
async def hello_world():
    return "Hello World"

# getting all students
@student_router.get('/students')
async def find_all_students():
    return listOfStudentEntity(connection.local.student.find())

# get one student with matching id
@student_router.get('/students/{studentId}')
async def find_student_by_id(studentId):
    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# creating a student
@student_router.post('/students')
async def create_student(student: Student):
    # convert to dictionary
    connection.local.student.insert_one(dict(student))
    return listOfStudentEntity(connection.local.student.find())

# update student
@student_router.put('/students/{studentId}')
async def update_student(studentId, student: Student):
    # find the student and than update it with new student data
    connection.local.student.find_one_and_update(
        {"_id": ObjectId(studentId)}, #object id to convert student id to id_
        {"$set": dict(student)} # convert all set in a dictionary
    )

    return studentEntity(connection.local.student.find_one({"_id": ObjectId(studentId)}))

# delete a student we need a studentId
@student_router.delete('/students/{studentId}')
async def delete_student(studentId):
    #finds the student deletes it and also returns the same student object
    return studentEntity(connection.local.student.find_one_and_delete({"_id": ObjectId(studentId)}))






