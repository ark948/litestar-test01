from litestar import Litestar, get
from litestar.exceptions import HTTPException
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



# filtering data using query parameters
# making query parameter optional


@get("/list")
async def get_list(done: bool | None = None) -> list[TodoItem]:
    if done is None:
        return TODO_LIST
    return [item for item in TODO_LIST if item.done == done]


app = Litestar(
    [index, get_list]
)


