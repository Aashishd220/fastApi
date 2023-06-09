from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()







students={
    1:{
        "name":"john",
        "age":13,
        "year":"year 12"
    }
}

class Student(BaseModel):
    name:str
    age:int
    year:str

class UpdateStudent(BaseModel):
    name:Optional[str]=None
    age: Optional[int]=None
    year: Optional[str]=None

@app.get("/get-student/{studentId}")
def getSudent(studentId:int=Path(...,description="Enter student ID",gt=0)):
    return students[studentId]

@app.get("/get-by-name")
def get_student(*,name:Optional[str]=None ,age :int):
    for studentId in students:
        if students[studentId]["name"] ==name:
            return students[studentId]
    return {"Data":"Not found"}


@app.post("/create-student/{studentId}")
def createStudent(studentId : int,student:Student):
    if studentId in students:
        return {"Error":"Student already present"}
    students[studentId]=student
    return students[studentId]


@app.put("/update-student/{studentId}")
def updateStudent(studentId: int,student:UpdateStudent):
    if studentId not in students:
        return {"Error":"Student not present"}
    students[studentId]=student
    return students[studentId]

@app.delete("/delete-student/{studentId}")
def deleteStudent(studentId:int):
    if studentId not in students:
        return {"Error":"Student not exist"}
    del students[studentId]
    return {"Message":"Student Deleted Successfully!!"}