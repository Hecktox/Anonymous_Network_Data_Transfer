import socket
import json
import threading
from typing import Optional

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
                            print("got ip req")
                            is_ip_request = True
                            conn.sendall(str(self.cypherClient.get_public_key()).encode("utf-8"))
                            break

                        messageRecieved += data

                        if data.endswith(self.msg_ending.encode("utf-8")):
                            # conn.sendall(b"yes i exist, im node 4")
                            conn.close()
                            break

                    if not is_ip_request:
                        print(f"received msg: {messageRecieved}")
                        msg = messageRecieved[0:-len(self.msg_ending)]
                        newHost, newPort = self.get_next_ip(msg)
                        print(newHost)
                        print(newPort)
                        print("REEEEEE")
                        if newHost is not None and newPort is not None:
                            self.send_msg(HOST=newHost, PORT=newPort, msg=msg)


    # def treat_msg(self, msg):
    #     if msg.decode("utf-8").startswith("whats_you_ip"):
    #         pass
    #     else:
    #         self.get_next_ip(msg)

    def get_next_ip(self, msg: bytes) -> tuple:
        data = json.loads(msg.decode("utf-8"))
        print(data)

        for ip in data["ips"]:

            try:
                private_key = self.cypherClient.get_private_key()
                decryptedIp = self.cypherClient.decrypt(ip, private_key)
                print(f"found {decryptedIp}")
                if decryptedIp == f"{self.HOST}:{self.PORT}":
                    print(F"RECEIVED MESSAGE: {self.cypherClient.decrypt(data['msg'], private_key)}")
                    return None, None
                else:
                    print("but i just return")
                    return decryptedIp.split(":")
            except Exception as e:
                print(f"THERES ERROR : {e}")
                continue
        print("WTFFFFFF??????")
        return None, None


    # def ask_for_pub(self, HOST, PORT):
    #     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #         print(f"sending to: {HOST}:{PORT}")
    #         s.connect((str(HOST), int(PORT)))
    #         # s.sendall(msg.encode("utf-8"))
    #         # print("BRO LOOK HERE")
    #         # print(msg)
    #         s.sendall("whats_your_pub_key".encode("utf-8"))
    #         s.sendall(self.msg_ending.encode("utf-8"))
    #         data = s.recv(1024)
    #         # print(f"Received {data!r}")
    #         return data

    def send_msg(self, msg: Optional[str]=None, HOST='', PORT=''):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # print(HOST)
            # print(PORT)
            print(f"sending to: {HOST}:{PORT}")
            s.connect((str(HOST), int(PORT)))
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
