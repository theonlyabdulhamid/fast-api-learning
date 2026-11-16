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