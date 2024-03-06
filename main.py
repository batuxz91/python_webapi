# Documentacion oficial: https://fastapi.tiangolo.com/

# Instalacion FastAPI: pip install fastapi
# Instalacion Uvicorn: pip install "uvicorn[standard]"

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello World"}

#


@app.get("/url")
async def url():
    return {"url:https://google.com"}
