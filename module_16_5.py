from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Инициализация Jinja2Templates
templates = Jinja2Templates(directory="templates")

# Список пользователей
users = []

# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int

# Функция для получения следующего ID
def get_next_id():
    return users[-1].id + 1 if users else 1

# Главная страница: список пользователей
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

# Получение пользователя по ID
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def get_user(request: Request, user_id: int):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})

# DELETE запрос для удаления пользователя
@app.delete("/user/{user_id}", response_model=User)
def delete_user(user_id: int):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")

# Добавление пользователя
@app.post("/user/{username}/{age}", response_model=User)
def create_user(username: str, age: int):
    new_id = get_next_id()
    user = User(id=new_id, username=username, age=age)
    users.append(user)
    return user

#PUT запрос для обновления пользователя
@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


# Заполнение списка пользователей для начального состояния
create_user("UrbanUser", 24)
create_user("UrbanTest", 22)
create_user("Capybara", 60)



