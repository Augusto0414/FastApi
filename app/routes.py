from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import TodoCreate, Todo
from prisma import Prisma
from prisma.models import Todo as PrismaTodo

router = APIRouter()
prisma = Prisma()

@router.post("/todo/", response_model=Todo,  status_code=status.HTTP_201_CREATED)
async def create_todo_route(todo: TodoCreate):
    """Crear un nuevo todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        created_todo = await prisma.todo.create(
            data={
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
        )
        
        return {
            'id': created_todo.id,
            'title': created_todo.title,
            'description': created_todo.description,
            'completed': created_todo.completed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/todo/", response_model=List[Todo])
async def read_all_todos():
    """Obtener todos los todos"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        todos = await prisma.todo.find_many()
        return [
            {
                'id': todo.id,
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
            for todo in todos
        ] if todos else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/todo/{todo_id}", response_model=Todo)
async def read_todo_route(todo_id: str):
    """Obtener un todo por ID"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        todo = await prisma.todo.find_unique(
            where={
                'id': todo_id
            }
        )
        
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")
            
        return {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed
        }
    except prisma.errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put("/todo/{todo_id}", response_model=Todo)
async def update_todo_route(todo_id: str, todo: TodoCreate):
    """Actualizar un todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        # Primero verificamos si el todo existe
        existing_todo = await prisma.todo.find_unique(
            where={
                'id': todo_id
            }
        )
        
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        updated_todo = await prisma.todo.update(
            where={
                'id': todo_id
            },
            data={
                'title': todo.title,
                'description': todo.description,
                'completed': todo.completed
            }
        )
        
        return {
            'id': updated_todo.id,
            'title': updated_todo.title,
            'description': updated_todo.description,
            'completed': updated_todo.completed
        }
    except prisma.errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/todo/{todo_id}")
async def delete_todo_route(todo_id: str):
    """Eliminar un todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        # Primero verificamos si el todo existe
        existing_todo = await prisma.todo.find_unique(
            where={
                'id': todo_id
            }
        )
        
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo not found")

        await prisma.todo.delete(
            where={
                'id': todo_id
            }
        )
        return {"message": "Todo deleted successfully"}
    except prisma.errors.RecordNotFoundError:
        raise HTTPException(status_code=404, detail="Todo not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))