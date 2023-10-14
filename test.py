import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 10000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")


while True:
    print("a")

# string = "Hello World"
#
# # string with encoding 'utf-8'
# messageToByte = bytes(string, 'utf-8')
#
# print(messageToByte,'\n')
#
# byteToMessage = messageToByte.decode("utf-8")
#
# print(byteToMessage)
#
# def toByte(string):
#     return


