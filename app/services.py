from prisma import Prisma
from app.models import TodoCreate, Todo

prisma = Prisma()

async def create_todo(todo: TodoCreate) -> Todo:
    """Crear un nuevo todo"""
    return await prisma.todo.create(
        data={
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed
        }
    )

async def get_all_todos() -> list[Todo]:
    """Obtener todos los todos"""
    return await prisma.todo.find_many()

async def get_todo_by_id(todo_id: str) -> Todo | None:
    """Obtener un todo por ID"""
    return await prisma.todo.find_unique(where={'id': todo_id})

async def update_todo(todo_id: str, todo: TodoCreate) -> Todo:
    """Actualizar un todo"""
    return await prisma.todo.update(
        where={'id': todo_id},
        data={
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed
        }
    )

async def delete_todo(todo_id: str) -> None:
    """Eliminar un todo"""
    await prisma.todo.delete(where={'id': todo_id})
