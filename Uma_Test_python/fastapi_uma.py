from fastapi import FastAPI

app=FastAPI()

@app.get("/hello")

def welcome():
    return{"Welcome to FastAPI Uma"}