import socket


class SocketMan:
    def __init__(self, HOST=None, PORT=None):
        self.HOST = HOST
        self.PORT = PORT

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
                        if not data:
                            print("raaaaaa")
                            conn.sendall(b"close")
                            break
                        # print(data)
                        messageRecieved += data
                        # conn.close()
                        conn.sendall(b"close")
                    print("done: ")
                    print(messageRecieved)

    def get_next_ip(self):
        pass

    def send_msg(self, msg, HOST, PORT):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(msg.encode("utf-8"))
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