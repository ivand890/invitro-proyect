from fastapi import FastAPI
from app.routers import review

app = FastAPI(title="Product Review Feedback Service")
app.include_router(review.router)
