from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel, Field, EmailStr

app = FastAPI()
users_db = []


class UserRequest(BaseModel):
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(ge=18, le=100)


class UserResponse(BaseModel):
    name: str
    email: EmailStr
    age: int


class UserUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=3,
        max_length=50
    )
    email: EmailStr | None =None
    age: int | None = Field(
        default=None,
        ge=18,
        le=100
    )

class UserCreatedResponse(BaseModel):
    message: str
    user: UserResponse

class UserUpdatedResponse(BaseModel):
    message:str
    user:UserResponse
@app.post(
    "/users", status_code=status.HTTP_201_CREATED, response_model=UserCreatedResponse
)
def create_users(data: UserRequest):
    user = {"name": data.name, "email": data.email, "age": data.age}
    users_db.append(user)
    return {"message": "User created successfully", "user": user}


@app.get("/users", response_model=list[UserResponse])
def get_users():
    return users_db


@app.get("/users/{user_id}", response_model=UserResponse)
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
    return {"message": "User updated successfully", "user": UserUpdatedResponse}


@app.put("/users/{user_id}")
def replace_user(user_id: int, data: UserRequest):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    user = users_db[user_id - 1]
    updated_data = data.model_dump()
    users_db[user_id - 1] = updated_data
    return {"message": "User updated successfully", "user": updated_data}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(users_db):
        raise HTTPException(status_code=404, detail="User not found")
    users_db.pop(user_id - 1)
    return "Deleted"

