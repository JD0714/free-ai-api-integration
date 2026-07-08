import os
from dotenv import load_dotenv

load_dotenv()

SERVER_URL = (
    f"http://{os.getenv('SERVER_IP')}:{os.getenv('SERVER_PORT')}/command"
)