from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

user_db : Dict[str,dict] = {}

class UserRegister(BaseModel):
    name:str
    password:str
    info:str

class UserLogin(BaseModel):
    name:str
    password:str

@app.get("/hello")
async def hello():
    return {"message": "Hello"}

@app.post("/resigner")
async def register(user:UserRegister):

    try:
        if user.name in user_db:
            return "already"
        else:
            user_db[user.name] = {"password":user.password,"info":user.info}
            return "ok"
    except Exception as e:
        return "failed"

@app.post("/login")
async def login(user:UserLogin):

    try:
        if user.name not in user_db:
            return "resigner first"

        in_users = user_db[user.name]

        if user.password == in_users["password"]:
            print(in_users["info"])
            return "ok"
        else:
            return "password wrong"
    except Exception as e:
        print(f"登录失败:{e}")
        return "failed"

import uvicorn

uvicorn.run(app, host="127.0.0.1", port=11451)