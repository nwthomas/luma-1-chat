from src.server import app
from src.constants import *

if __name__ == '__main__':
    app.run(port=SERVER_PORT)