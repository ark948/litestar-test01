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

@get("/list")
async def get_list(done: str) -> list[TodoItem]:
    if done == "1":
        return [item for item in TODO_LIST if item.done]
    if done == "0":
        return [item for item in TODO_LIST if not item.done]
    raise HTTPException(f"Invalid query parameter value: {done!r}", status_code=400)



app = Litestar(
    [index, get_list]
)


