# ДЗ 16_2: "Валидация данных"

# Задача "Аннотация и валидация"

from fastapi import FastAPI, Path
from typing import Annotated


# uvicorn module_16_2:app --reload -  команда для запуска сервера из терминала


# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
#async def root()
async def main_page():
    return "Главная страница"

# Создаем маршрут к странице администратора
@app.get("/user/admin")
async def read_adm():
    return "Вы вошли как администратор"

# Создаrv маршрут к страницам пользователей,
# используя параметр в пути - "/user/{user_id}"
@app.get("/user/{user_id}")
async def read_user_id(
        user_id: Annotated[int, Path(ge=1,              # >1 or = 1
                                     le=100,
                                     description="Enter User ID")]
):
    return f"Вы вошли как пользователь № {user_id}"

# Создаем маршрут к страницам пользователей,передавая данные
# в адресной строке - "/user"
@app.get("/user/{username}/{age}")
async def read_user(
        username: Annotated[str, Path(min_length=5,
                                      max_length=20,
                                      description="Enter username")],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description="Enter age")]
):
    return f"Информация о пользователе- Имя: {username}, Возраст: {age}"