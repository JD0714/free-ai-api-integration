import requests
from config import SERVER_URL


action = input(
    "Enter command (start/continue/end): "
)

text = input(
    "Enter your string: "
)


data = {
    "action": action,
    "text": text
}


response = requests.post(
    SERVER_URL,
    json=data
)


print(response.json()["status"])