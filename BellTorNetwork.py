import socket
import json
import threading
from RSA_cypher import RSA_cypher


class SocketMan:
    def __init__(self, nodeId, HOST=None, PORT=None):
        self.nodeId = nodeId
        self.cypherClient = RSA_cypher(nodeId)
        self.HOST = HOST
        self.PORT = PORT
        self.msg_ending = "|close"

    def listen_for_msg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()

            print("Started!")
            print(f"Listening on {self.HOST}:{self.PORT}")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            conn.close()
                            break
                        print(data)
                        # conn.close()
                        conn.sendall(b"close")

    def listen_and_forward(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen()

            print("Started!")
            print(f"Listening on {self.HOST}:{self.PORT}")

            while True:
                conn, addr = s.accept()
                with conn:
                    print(f"Connected by {addr}")
                    messageRecieved = b""

                    is_ip_request = False

                    while True:
                        data = conn.recv(1024)
                        # print(data.decode("utf-8"))
                        if "whats_your_pub_key" in data.decode("utf-8"):
                            is_ip_request = True
                            print("AAAAAAAAAAAAAAA")
                            conn.sendall(str(self.cypherClient.get_public_key()).encode("utf-8"))
                            break

                        messageRecieved += data

                        if data.endswith(self.msg_ending.encode("utf-8")):
                            print("raaaaaa")
                            # conn.sendall(b"yes i exist, im node 4")
                            conn.close()
                            break

                    print("done: ")
                    # print(messageRecieved)

                    if not is_ip_request:
                        msg = messageRecieved[0:-len(self.msg_ending)]
                        newHost, newPort = self.get_next_ip(msg)
                        self.send_msg(newHost, newPort, msg)


    # def treat_msg(self, msg):
    #     if msg.decode("utf-8").startswith("whats_you_ip"):
    #         pass
    #     else:
    #         self.get_next_ip(msg)

    def get_next_ip(self, msg):
        data = json.loads(msg.decode("utf-8"))
        print(data)

        for ip in data["ips"]:
            print(ip)

            # TODO: Check if you can decrypt the ip, if yes then proceed with it, else continue
            # newHost, newPort = ip.split(":")
            # self.send_msg(msg, newHost, int(newPort))
            return ip.split(":")


    def send_msg(self, msg, HOST, PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # s.sendall(msg.encode("utf-8"))
            # print("BRO LOOK HERE")
            # print(msg)
            if type(msg) is bytes:
                s.sendall(msg)
            else:
                s.sendall(json.dumps(msg).encode('utf-8'))
            s.sendall(self.msg_ending.encode("utf-8"))
            data = s.recv(1024)
            # print(f"Received {data!r}")
            return data

    def create_network_message(self, msg, listIps):
        # format:
        # {
        #  listIps: [dsf, sdf, s,df],
        #  message : "asdfoiushogfusa"
        # }

        data = {}
        data['ips'] = listIps
        data['msg'] = msg

        return data

    def run_server(self):
        t1 = threading.Thread(target=self.listen_and_forward).start()
