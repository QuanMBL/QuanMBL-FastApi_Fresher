from fastapi import FastAPI

app = FastAPI()

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/A")
async def get_a():
    return {"message": "hello world"}
