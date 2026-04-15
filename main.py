from fastapi import FastAPI
from routes.app_routes import app_routes

app = FastAPI()

app.include_router(app_routes)