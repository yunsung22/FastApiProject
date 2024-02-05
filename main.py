from fastapi import FastAPI

from app.routes.board import board_router
from app.routes.member import member_router

app = FastAPI()

app.include_router(member_router)
app.include_router(board_router, prefix='/board')

@app.get("/")
async def index():
    return {"message": "Hello World"}


# 파이썬 코드로
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)