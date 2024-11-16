from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import mysql.connector
import datetime

mydb = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password = "",
    database = "2024_fast_api_student"
)

cursor = mydb.cursor()

app = FastAPI()

class DBModel(BaseModel):
    name: str
    address: Optional[str] = ''
    class_name: str = None

## API endpoints

## Get all student info
@app.get('/student')
def get_all_students():
    cursor.execute("select * from student_info")
    result = cursor.fetchall()
    return result

## Insert new student data
@app.post('/student/add')
def add_new_student(user: DBModel):
    insert_query = '''
        insert into student_info (name, address, class_name, created_on)
        values (%s, %s, %s, %s)
    '''
    values = (user.name, user.address, user.class_name, datetime.datetime.now())

    try:
        cursor.execute(insert_query, values)
        mydb.commit()
    except mysql.connector.Error as err:
        mydb.rollback()
        raise HTTPException(status_code = 400, detail = f"Error: {err}")
    
    return {"message": "student info is registered successfully"}

## Update a student data
@app.put('/student/{id}')
def update_student(id:int, student_data: DBModel):
    update_query = '''
    update student_info set name = %s, address = %s, class_name = %s 
    where id = %s
    '''
    values = (student_data.name, student_data.address, student_data.class_name, id)
    
    try:
        cursor.execute(update_query, values)
        mydb.commit()
    except mysql.connector.Error as err:
        mydb.rollback()
        raise HTTPException(status_code = 404, detail = f"Error : {err}")
    
    return {"message": "Student info is updated successfully"}

## Delete a student data
@app.delete('/student/{id}')
def delete_student_info(id:int):
    query = '''Delete from student_info where id = %s'''
    
    try:
        cursor.execute(query, (id,))
        mydb.commit()
    except mysql.connector.Error as err:
        mydb.rollback()
        raise HTTPException(status_code = 404, detail = f"Error: {err}")
    
    return {"message": "student record is deleted successfully"} 