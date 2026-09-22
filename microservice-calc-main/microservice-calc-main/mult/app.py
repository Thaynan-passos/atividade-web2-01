from fastapi import FastAPI
import os

app = FastAPI()

CONTAINER_NAME = os.getenv("HOSTNAME", "unknown")


@app.get("/mult")
def multiplicacao(op1: float, op2: float):
    return {
        "op1": op1,
        "op2": op2,
        "resultado": op1 * op2,
        "container": CONTAINER_NAME
    }