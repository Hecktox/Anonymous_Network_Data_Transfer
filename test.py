from BellTorNetwork import SocketMan
import socket
import threading
import random
import json

# HOST = "127.0.0.1"  # The server's hostname or IP address
# HOST = "192.168.1.40"
HOST = "172.20.24.32"
# HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999  # The port used by the server

nodeId = 2

client = SocketMan(nodeId, HOST, PORT)

# t1 = threading.Thread(target=client.listen_for_msg).start()


destHOST = "172.20.24.32"
# destHOST = "192.168.1.40"
# destPORT = 10000
destPORT = 10001

myAddress = f"{HOST}:{PORT}"

with open("list_of_nodes.txt", 'r') as file:
    list_of_nodes = file.readline().strip().split(", ")
    random.shuffle(list_of_nodes)

    list_of_nodes.insert(0, f"{HOST}:{PORT}")
    list_of_nodes.append(f"{destHOST}:{destPORT}")

print(list_of_nodes)
# encrypt the ips in the list
for i in range(len(list_of_nodes)):
    if i == 0 or list_of_nodes[i - 1] == myAddress:
        pubKey = client.cypherClient.get_public_key()
        # print("my own")
    else:
        address = list_of_nodes[i - 1].split(":")
        # print(f"address: {address}")
        pubKey = client.send_msg("whats_your_pub_key", address[0], int(address[1])).decode("utf-8")
    print(f"PUB HERE : {pubKey}")

# print(pubKey)

exit(0)

# client.send_msg("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbb", destHOST, destPORT)
msg = client.create_network_message("hello world! hows the weather?", ["192.168.1.40:10001"])
client.send_msg(msg, destHOST, destPORT)
# client.send_msg("whats_your_pub_key", destHOST, destPORT)



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


