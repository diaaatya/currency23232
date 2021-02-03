# main.py
from fastapi import FastAPI
app = FastAPI()

@app.get("/rates")
def hello():
    return {"USD":"15.8 ",
            "EUR": "20.01"}
