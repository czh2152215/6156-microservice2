from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn
from db_connection import SessionLocal
from models.Adopter import Adopter
from fastapi import HTTPException


app = FastAPI()
session = SessionLocal()
class AdopterOut(BaseModel):
    id:int
    name:str
    age:int
    email:str
    phone:str
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/adopter/{adopter_id}", response_model=AdopterOut)
def get_adopter(adopter_id: int):
    try:
        adopter = session.query(Adopter).filter(Adopter.id == adopter_id).first()
        if adopter is None:
            raise HTTPException(status_code=404, detail="Adopter not found")
        return adopter
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)