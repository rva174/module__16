# ДЗ 16_1: "Основы Fast Api и маршрутизация"
# Задача "Начало пути"

from fastapi import FastAPI


# uvicorn module_16_1:app --reload -  команда для запуска сервера из терминала


# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
#async def root()
async def main_page():
    return {"message": "Главная страница"}

# Создаем маршрут к странице администратора
@app.get("/user/admin")
async def read_adm():
    return {"message": "Вы вошли как администратор"}

# Создаrv маршрут к страницам пользователей,
# используя параметр в пути - "/user/{user_id}"
@app.get("/user/{user_id}")
#async def read_user(user_id):
async def root(user_id):
    return {f"Вы вошли как пользователь № {user_id}"}

# Создаем маршрут к страницам пользователей передавая данные
# в адресной строке - "/user"
@app.get("/user")
async def read_user(username, age):
    return {f"Информация о пользователе- Имя: {username}, Возраст: {age}"}