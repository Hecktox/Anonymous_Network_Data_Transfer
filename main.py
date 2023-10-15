# THIS IS SERVER ONLY

from BellTorNetwork import SocketMan
import socket
import threading

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = socket.gethostbyname(socket.gethostname())
PORT = 10000  # Port to listen on (non-privileged ports are > 1023)

print("Starting...")

socketServer = SocketMan(HOST, PORT)

# socketServer.listen_for_msg()
t1 = threading.Thread(target=socketServer.listen_and_forward).start()
print("a")

