from src.server import app
from dotenv import load_dotenv
from src.constants import *
import os

load_dotenv()
SERVER_HOST=os.getenv("SERVER_HOST")

if __name__ == '__main__':
    app.run(host=SERVER_HOST, port=SERVER_PORT)