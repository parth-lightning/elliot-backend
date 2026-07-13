from fastapi import FastAPI
from app.api.routes import router


app = FastAPI(
    title="Automated UI/UX Review Agent",
    description="AI agent for automated UI/UX analysis",
    version="1.0.0"
)


app.include_router(router)


@app.get("/")
def home():
    return {
        "message": "Automated UI/UX Review Agent API is running!"
    }