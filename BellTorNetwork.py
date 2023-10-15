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
                    while True:
                        data = conn.recv(1024)
                        messageRecieved += data

                        if data.endswith(self.msg_ending.encode("utf-8")):
                            print("raaaaaa")
                            # conn.sendall(b"yes i exist, im node 4")
                            conn.close()
                            break

                    print("done: ")
                    print(messageRecieved)

                    # if "whats_you_ip" in data.decode("utf-8"):
                    #     print("AAAAAAAAAAAAAAA")
                    #     conn.sendall(self.cypherClient.get_public_key().encode("utf-8"))
                    #     break

                    self.get_next_ip(messageRecieved)

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


    def send_msg(self, msg, HOST, PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            # s.sendall(msg.encode("utf-8"))
            s.sendall(json.dumps(msg).encode('utf-8'))
            s.sendall(self.msg_ending.encode("utf-8"))
            print(f"Received {s.recv(1024)!r}")

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
