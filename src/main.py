from fastapi import FastAPI
from routes import student
from core.middleware import add_middlewares

app = FastAPI()
add_middlewares(app)
app.include_router(student.router)