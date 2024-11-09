from pydantic import BaseModel, Field
from typing import Annotated

class TodoBase(BaseModel):
    title: str
    description: str
    completed: bool = False

class TodoCreate(TodoBase):
    pass

class Todo(BaseModel):
    id: Annotated[str, Field(order=0)]
    title: Annotated[str, Field(order=1)]
    description: Annotated[str, Field(order=2)]
    completed: Annotated[bool, Field(order=3)]

    class Config:
        from_attributes = True
        json_encoders = {
            # personalizamos la codificación JSON
            dict: lambda v: dict(sorted(v.items(), key=lambda x: getattr(Todo.model_fields[x[0]], "json_schema_extra", {}).get("order", 999)))
        }