from fastapi import FastAPI
from routers import user
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(user.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", tags=["root"])
async def root():
    return [{"mensaje": "Bienvenido a FastApi"},
            {"url": "http://localhost:8000"},
            {"documentacion": "http://localhost:8000/docs"}]
