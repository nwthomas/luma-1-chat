from . import server
from ..constants import *

if __name__ == "__main__":
    server.run_server(port=SERVER_PORT)