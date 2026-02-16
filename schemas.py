from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str

class TodoCreate(TodoBase):
    pass


class Todo(TodoBase):
    id: int

    class config:
        from_attributes = True