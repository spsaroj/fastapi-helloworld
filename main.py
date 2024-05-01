from fastapi import FastAPI
from app.views.task_view import router as item_router

app = FastAPI()

# Include item routes
app.include_router(item_router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)