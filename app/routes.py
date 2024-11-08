from fastapi import APIRouter, HTTPException
from typing import List
from app.models import TodoCreate, Todo
from prisma import Prisma

router = APIRouter()

prisma = Prisma()

@router.post("/todo/", response_model=Todo)
async def create_todo_route(todo: TodoCreate):
    """Crear un nuevo todo"""
    try:
        # Verificar que Prisma esté conectado
        if not prisma.is_connected():
            await prisma.connect()

        created_todo = await prisma.todo.create(
            data={
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
        )
        return created_todo
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/todo/", response_model=List[Todo])
async def read_all_todos():
    """Obtener todos los todos"""
    try:
        todos = await prisma.todo.find_many()  
        return todos
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/todo/{todo_id}", response_model=Todo)
async def read_todo_route(todo_id: str):
    """Obtener un todo por ID"""
    try:
        todo = await prisma.todo.find_unique(where={"id": todo_id})
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/todo/{todo_id}", response_model=Todo)
async def update_todo_route(todo_id: str, todo: TodoCreate):
    """Actualizar un todo"""
    try:
        updated_todo = await prisma.todo.update(
            where={"id": todo_id},
            data={
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
        )
        return updated_todo
    except Exception as e:
        raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/todo/{todo_id}")
async def delete_todo_route(todo_id: str):
    """Eliminar un todo"""
    try:
        await prisma.todo.delete(where={"id": todo_id})
        return {"message": "Todo deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=404, detail="Todo not found")
