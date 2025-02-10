from litestar import Litestar, get
from dataclasses import dataclass



@dataclass
class TodoItem:
    title: str
    done: bool


TODO_LIST: list[TodoItem] = [
    TodoItem(title="Start writing TODO list", done=True),
    TodoItem(title="???", done=False),
    TodoItem(title="Profit", done=False),
]



@get('/')
async def index() -> str:
    return "Hello World."



@get("/list")
async def get_list() -> list[TodoItem]:
    return TODO_LIST



app = Litestar(
    [index, get_list]
)


