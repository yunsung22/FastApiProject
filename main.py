from fastapi import FastAPI

from app.routes.member import member_router

app = FastAPI()

app.include_router(member_router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 파이썬 코드로
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)