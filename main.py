from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()
users_db = []


class UserRequest(BaseModel):
    name: str
    email: str
    age: int


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    age: int | None = None


@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_users(data: UserRequest):
    user = {"name": data.name, "email": data.email, "age": data.age}
    users_db.append(user)
    return {"message": "User created successfully", "user": user}


@app.get("/users")
def get_users():
    return users_db


@app.get("/users/{user_id}")
def get_user_id(user_id: int):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id - 1]


@app.patch("/users/{user_id}")
def update_user(user_id: int, data: UserUpdate):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[user_id - 1]
    updated_data = data.model_dump(exclude_unset=True)
    user.update(updated_data)
    return {"message": "User updated successfully", "user": user}

@app.put("/users/{user_id}")
def replace_user(user_id:int,data: UserRequest):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[user_id - 1]
    updated_data = data.model_dump()
    users_db[user_id - 1]=updated_data
    return {"message": "User updated successfully", "user": user}

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(user_id-1)
    return("Deleted")
