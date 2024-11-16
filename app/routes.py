from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import TodoCreate, Todo
from prisma import Prisma
from prisma.models import Todito as PrismaTodito  # Cambiado para reflejar tu modelo

router = APIRouter()
prisma = Prisma()

@router.post("/todo/", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo_route(todo: TodoCreate):
    """Crear un nuevo todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        created_todo = await prisma.todito.create(  # Cambiado a `todito` para reflejar la tabla
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
        raise HTTPException(status_code=500, detail=f"Error al crear el todo: {str(e)}")

@router.get("/todo/", response_model=List[Todo])
async def read_all_todos():
    """Obtener todos los todos"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        todos = await prisma.todito.find_many()  # Cambiado a `todito`
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
        raise HTTPException(status_code=500, detail=f"Error al obtener los todos: {str(e)}")

@router.get("/todo/{todo_id}", response_model=Todo)
async def read_todo_route(todo_id: str):
    """Obtener un todo por ID"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        todo = await prisma.todito.find_unique(  # Cambiado a `todito`
            where={
                'id': todo_id
            }
        )
        
        if todo is None:
            raise HTTPException(status_code=404, detail="Todo no encontrado")
            
        return {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el todo: {str(e)}")

@router.put("/todo/{todo_id}", response_model=Todo)
async def update_todo_route(todo_id: str, todo: TodoCreate):
    """Actualizar un todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        # Verificar si el todo existe
        existing_todo = await prisma.todito.find_unique(  # Cambiado a `todito`
            where={
                'id': todo_id
            }
        )
        
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo no encontrado")

        updated_todo = await prisma.todito.update(  # Cambiado a `todito`
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
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar el todo: {str(e)}")

@router.delete("/todo/{todo_id}")
async def delete_todo_route(todo_id: str):
    """Eliminar un todo"""
    if not prisma.is_connected():
        await prisma.connect()

    try:
        # Verificar si el todo existe
        existing_todo = await prisma.todito.find_unique(  # Cambiado a `todito`
            where={
                'id': todo_id
            }
        )
        
        if existing_todo is None:
            raise HTTPException(status_code=404, detail="Todo no encontrado")

        await prisma.todito.delete(  # Cambiado a `todito`
            where={
                'id': todo_id
            }
        )
        return {"message": "Todo eliminado exitosamente"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar el todo: {str(e)}")
