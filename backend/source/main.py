from litestar import Litestar, get, post
from litestar.exceptions import HTTPException
from dataclasses import dataclass
from typing import Any



@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: list[TodoItem] = []



@get('/')
async def index() -> str:
    return "Hello World."



# filtering data using query parameters
# making query parameter optional


@get("/list")
async def get_list(done: bool | None = None) -> list[TodoItem]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]



@post("/")
async def add_item(data: TodoItem) -> list[TodoItem]:
    TODO_LIST.append(data)
    return TODO_LIST



app = Litestar(
    [index, get_list, add_item]
)


