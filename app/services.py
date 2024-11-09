# routes.py
from fastapi import APIRouter, HTTPException
from typing import List
from app.models import TodoCreate, Todo
from prisma import Prisma

router = APIRouter()
prisma = Prisma()

async def create_todo(todo: TodoCreate) -> dict:
    """Crear un nuevo todo"""
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

async def get_all_todos() -> list[dict]:
    """Obtener todos los todos"""
    todos = await prisma.todo.find_many()
    
    return [
        {
            'id': todo.id,
            'title': todo.title,
            'description': todo.description,
            'completed': todo.completed
        }
        for todo in todos
    ]

async def get_todo_by_id(todo_id: str) -> dict | None:
    """Obtener un todo por ID"""
    todo = await prisma.todo.find_unique(where={'id': todo_id})
    if not todo:
        return None
        
    return {
        'id': todo.id,
        'title': todo.title,
        'description': todo.description,
        'completed': todo.completed
    }

async def update_todo(todo_id: str, todo: TodoCreate) -> dict:
    """Actualizar un todo"""
    updated_todo = await prisma.todo.update(
        where={'id': todo_id},
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