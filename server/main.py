from fastapi import FastAPI
from pydantic import BaseModel
from commands import handle_command

app = FastAPI()


class Command(BaseModel):
    action: str
    text: str


@app.post("/command")
def receive_command(command: Command):

    result = handle_command(
        command.action,
        command.text
    )

    return {
        "status": result
    }