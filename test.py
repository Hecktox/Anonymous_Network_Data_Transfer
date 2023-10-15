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

# client.send_msg("whats_your_pub_key", "192.168.38.214", 10001).decode("utf-8")
# exit(0)
# t1 = threading.Thread(target=client.listen_for_msg).start()


finaldestHOST = "172.20.24.32"
# destHOST = "192.168.1.40"
# destPORT = 10000
finaldestPORT = 10001

final_dest_pub_key = None

myAddress = f"{HOST}:{PORT}"

with open("list_of_nodes.txt", 'r') as file:
    list_of_nodes = file.readline().strip().split(", ")
    # random.shuffle(list_of_nodes)
    nextHOST = str(list_of_nodes[0].split(":")[0])
    nextPORT = int(list_of_nodes[0].split(":")[1])

    list_of_nodes.insert(0, f"{HOST}:{PORT}")
    list_of_nodes.append(f"{finaldestHOST}:{finaldestPORT}")

global encrMsg
encrMsg = ""
msgToSend = "hello world! hows the weather?"

def encrypt(list_ips):
    encryptedList = []
    list_ips.append(list_ips[-1])
    print(list_ips)
    # encrypt the ips in the list
    for i in range(len(list_ips)):
        if i == 0 or list_ips[i - 1] == myAddress:
            address = list_ips[i - 1]
            pubKey = client.cypherClient.get_public_key()
        else:
            address = list_ips[i - 1]
            pubKey = client.send_msg("whats_your_pub_key", str(address.split(":")[0]), int(address.split(":")[1])).decode("utf-8")
            # pubKey = client.ask_for_pub(str(address.split(":")[0]), int(address.split(":")[1]))

        if i == len(list_ips) - 1:
            # global encrMsg
            encrMsg = client.cypherClient.encrypt(msgToSend, pubKey)
        encryptedList.append(client.cypherClient.encrypt(address, pubKey))

    return encryptedList

encryptedList = encrypt(list_of_nodes)
print("encrypted:")
print(encryptedList)



# exit(0)

# client.send_msg("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbb", destHOST, destPORT)
# msg = client.create_network_message("hello world! hows the weather?", ["192.168.1.40:10001"])
msg = client.create_network_message(encrMsg, encryptedList)
client.send_msg(msg, nextHOST, nextPORT)
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


