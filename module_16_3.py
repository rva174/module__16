# 16_3. Домашнее задание по теме "CRUD Запросы: Get, Post, Put Delete."
# Задача "Имитация работы с БД"


from fastapi import FastAPI, Path
from typing import Dict, Annotated

app = FastAPI()

# Храним пользователей в словаре
users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users()->dict:
    return users


@app.post('/user/{username}/{age}')
async def create_user(
        username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name")],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age')]
):
    new_id = str(int(max(users, key=int)) + 1)
    users[new_id] = f'Имя: {username}, возраст: {age}'
    return f'User {new_id} is registered'

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        user_id: Annotated[int, Path( description="Enter id")],
        username: Annotated[str, Path(min_length=2, max_length=15, description="Enter name")],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age")]
):
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'

@app.delete('/user/{user_id}')
async def delete_user(
        user_id: Annotated[int, Path(description="Enter id")]
):
    users.pop(str(user_id))
    return f'User {user_id} is delete'

