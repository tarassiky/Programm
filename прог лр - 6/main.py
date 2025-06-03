from http.client import HTTPException
from typing import Union
from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from sqlmodel import Field, Session, SQLModel, create_engine, select
from contextlib import asynccontextmanager  # Import asynccontextmanager


app = FastAPI()

class Term(BaseModel):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str = Field(default='error')

glossary: dict[str,Term]={
    'REST': Term(
        name="REST",
        description = 'передача репрезентативного состояния'),
    'RPC': Term(
        name="RPC",
        description = 'Удаленный вызов процедур')
}

engine = None
engine = create_engine('mysql+pymysql://dasha:6767@db/lr6')

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

print(engine)

@asynccontextmanager  # Decorate with asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code
    print("Starting up the application...")
    create_db_and_tables()  # Run the database creation
    yield
    # Shutdown code (optional)
    print("Shutting down the application...")

app = FastAPI(lifespan=lifespan)  # Use lifespan for app lifecycle



@app.get('/dbconnect')
def get_db_info():
    return str(engine)

@app.get("/terms/{term}")
def get_term(term:str):
    if term not in glossary:
        raise HTTPException(status_code=404, detail = "Term not found")
    return glossary.get(term,"term not found")

@app.post("/terms/{term}",response_model=dict[str,Term])
def post_term(term: str, term_data: Term):
    if term in glossary:  # Corrected condition
        raise HTTPException(status_code=400, detail="Term already exists!")
    glossary[term] = term_data
    return {term: term_data}

@app.put("/terms/{term}",response_model=dict[str,Term])
def change_term(term:str,term_data:Term):
    if term not in glossary:
        raise HTTPException(status_code=400, detail = "Term not found!")
    glossary[term] = term_data
    return {term: term_data}

@app.delete("/terms/{term}")
def del_term(term:str):
    if term not in glossary:
        raise HTTPException(status_code=404, detail = "Term not found!")
    del glossary[term]
    return {"result":"deleted successfully"}

@app.get("/terms")
def all_get_term():
    return glossary
