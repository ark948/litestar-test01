from litestar import Litestar, get
from dataclasses import dataclass





TODO_LIST: list[dict[str, str | bool]] = [
    {"title": "Start writing TODO list", "done": True},
    {"title": "???", "done": False},
    {"title": "Profit", "done": False},
]




@get('/')
async def index() -> str:
    return "Hello World."



@get("/list")
async def get_list() -> list[dict[str, str | bool]]:
    return TODO_LIST



app = Litestar(
    [index, get_list]
)


