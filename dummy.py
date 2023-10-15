# THIS IS DUMMY NODE

from BellTorNetwork import SocketMan
import socket
import threading

nodeId = 3

# HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = "192.168.1.40"
PORT = 10001  # Port to listen on (non-privileged ports are > 1023)

print("Starting...")

dummy = SocketMan(nodeId, HOST, PORT)

# socketServer.listen_for_msg()
# t1 = threading.Thread(target=socketServer.listen_and_forward).start()

dummy.run_server()

print("a")

