# 16_3. Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Задача "Имитация работы с БД"


from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import Dict, Annotated

app = FastAPI()

# Храним пользователей в словаре
users = {'1': 'Имя: Example, возраст: 18'}


class User(BaseModel):
    username: str
    age: int


@app.get('/users')
async def get_users():
    return users


@app.post('/user/{username}/{age}')
async def create_user(username: str, age: int):
    # Проверка на корректность возраста
    if age < 18:
        raise HTTPException(status_code=400, detail="Возраст должен быть е меньше 18")

    # Находим следующий доступный ID
    new_id = str(max(map(int, users.keys())) + 1)

    # Добавляем нового пользователя
    users[new_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_id} is registered"


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(user_id: str, username: str, age: int):
    # Проверка на существование пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Проверка на корректность возраста
    if age < 18:
        raise HTTPException(status_code=400, detail="Возраст должен быть е меньше 18")

    # Обновляем данные
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete('/user/{user_id}')
async def delete_user(user_id: str):
    # Проверка на существование пользователя
    if user_id not in users:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")

    # Удаляем пользователя
    del users[user_id]
    return f"User {user_id} has been deleted"
