from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Task(BaseModel):
    task: str

tasks = []
#acesta este o ruta de baza,atunci cand apesi pe http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return{"message:" "Welcome to the Task API"}

#aceasta este ruta care obtine toate taskurile.Scopul acestei rute este să returneze lista de taskuri curente.
@app.get("/tasks")
def get_tasks():
    return tasks

# Ruta pentru adăugarea unui nou task
# dict() transformă un obiect Pydantic într-un dicționar (JSON)
@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task added"}

# Acest bloc de cod verifică dacă scriptul este rulat direct (nu importat ca modul).
# Dacă este rulat direct, importă uvicorn și pornește serverul ASGI(Asynchronous Server Gateway Interface) folosind uvicorn.
# Serverul va asculta pe adresa 127.0.0.1 (localhost) și portul 8000.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
