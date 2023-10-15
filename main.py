# THIS IS SERVER ONLY

from BellTorNetwork import SocketMan
import socket
import threading
from RSA_cypher import RSA_cypher

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
# HOST = socket.gethostbyname(socket.gethostname())
HOST = "192.168.1.40"
PORT = 10000  # Port to listen on (non-privileged ports are > 1023)

nodeId = 1

print("Starting...")

socketServer = SocketMan(nodeId, HOST, PORT)
socketServer.run_server()

# socketServer.listen_for_msg()
# t1 = threading.Thread(target=socketServer.listen_and_forward).start()
print("a")

