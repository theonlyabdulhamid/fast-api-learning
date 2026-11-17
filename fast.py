from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Abdulhamid!"}


@app.get("/profile")
def profile():
    return [
        {
            "name": "Abdulhamid",
            "country": "Nigeria",
            "Programinglanguage": "Python,javascript",
        },
    ]


@app.get("/projects")
def project():
    return ["Expense Tracker", "Quiz app", "AI chatbot", "To-Do List"]


@app.get("/skills")
def skills():
    return ["Python", "Javascript", "HTML", "CSS"]

@app.post("/users")
def user():
   return {"message": "User created"}






from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel 

app = FastAPI()

class MessageRequest(BaseModel):
    message:str



@app.post("/chats/{chat_id}/messages")
def send_message(chat_id:int,data:MessageRequest):
    return {
        "chat_id":chat_id,
        "user_message":data.message,
        "reply": "I recieved your message!"
    }

@app.post("/users",status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message":"User Created Successfully"}

chats={
    1:"Hello, how are you",
    2:"Explain Python",
    3:"What is FastAPI"
}

@app.get("/chat/{chat_id}")
def get_chat(chat_id:int):
    if chat_id not in chats:
        raise HTTPException(
            status_code=404,
            detail="Chat not found"
            )
    return {
        "chat_id": chat_id,
        "message": chats[chat_id]
    }