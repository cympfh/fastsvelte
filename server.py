import logging

from fastapi import FastAPI
from util.mount import MountFiles

app = FastAPI()
logger = logging.getLogger("uvicorn")


@app.get("/api/subscribe")
def subscribe(name: str, username: str, email: str, checked: bool):
    if checked:
        return {"status": "success", "name": name, "username": username, "email": email}
    return {"status": "failed", "error": "you need to agree"}


app.mount("/", MountFiles(directory="web/build/", html=True), name="static")
