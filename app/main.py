from fastapi import FastAPI
from app.routers import router

app = FastAPI(title="Product Review Feedback Service")
app.include_router(router)
