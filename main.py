from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


from app.routes.board import board_router
from app.routes.member import member_router

app = FastAPI()

app.include_router(member_router)
app.include_router(board_router, prefix='/board')

# jinja2 설정
templates = Jinja2Templates(directory='views/templates')


@app.get("/", response_class=HTMLResponse)
async def index(req: Request):
    return templates.TemplateResponse('index.html', {'request': req})


# 파이썬 코드로
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)