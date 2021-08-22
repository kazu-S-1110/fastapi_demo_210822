from fastapi import FastAPI
from api.routers import task, done

app = FastAPI()


@app.get("/hello")
async def hello():
    return {"message": "hello, world!, how r y?"}

app.include_router(task.router)
app.include_router(done.router)
