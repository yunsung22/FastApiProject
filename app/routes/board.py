from fastapi import FastAPI, APIRouter

board_router = APIRouter()

@board_router.get('/list')
def list():
    return {'msg': 'Hello, board list!'}


@board_router.get('/write')
def write():
    return {'msg': 'Hello, board write!'}


@board_router.get('/view')
def view():
    return {'msg': 'Hello, board view!'}