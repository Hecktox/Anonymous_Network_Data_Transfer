from flask import Flask, render_template, request
from BellTorNetwork import SocketMan

app = Flask(__name__, template_folder='templates')

HOST = "192.168.56.1"
# HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999  # The port used by the server

nodeId = 4

client = SocketMan(nodeId, HOST, PORT)


# A list to store added IPs
added_ips = []

@app.route('/')
def index():
    return render_template('Page1.html', added_ips=added_ips)

@app.route('/Page2', methods = ['GET', 'POST'])
def about():
    # if request.method == 'POST':
    #     user = request.form['nm']
    #     print(user)
    #     return index
    # else:
    return render_template('Page2.html')


@app.route('/add_ip', methods=['POST'])
def add_ip():
    new_ip = request.form.get('newIP')
    if new_ip and new_ip.strip():
        added_ips.append(new_ip)
        # update_node_file()
    return index()

@app.route('/send-message', methods = ['GET','POST'])
def send_message():
    # msg = request.args.get('messageInput')
    # msg = request.form["messageInput"]
    # new_ip = request.args.get('addressInput')
    address = request.form['addressInput']
    msg = request.form['messageInput']

    print(msg)
    print(address)

    handle_send_msg(msg, address)

    # return about()
    return ('', 204)

def update_node_file():
    try:
        with open('list_of_nodes.txt', 'w+') as f:
            ip_string = ', '.join(added_ips)
            f.write(ip_string)
    except Exception as e:
        print("Error writing to file: {}".format(str(e)))


def handle_send_msg(msgToSend, finaldestAddress):
    final_dest_pub_key = None

    myAddress = f"{HOST}:{PORT}"

    with open("list_of_nodes.txt", 'r') as file:
        list_of_nodes = file.readline().strip().split(", ")
        # random.shuffle(list_of_nodes)
        nextHOST = str(list_of_nodes[0].split(":")[0])
        nextPORT = int(list_of_nodes[0].split(":")[1])

        list_of_nodes.insert(0, f"{HOST}:{PORT}")
        list_of_nodes.append(f"{finaldestAddress}")

    # msgToSend = "hello world! hows the weather?"

    def encrypt(msg, list_ips):
        encryptedList = []
        list_ips.append(list_ips[-1])
        print(list_ips)
        # encrypt the ips in the list
        encrMsg = ""
        for i in range(len(list_ips)):
            if i == 0 or list_ips[i - 1] == myAddress:
                address = list_ips[i - 1]
                pubKey = client.cypherClient.get_public_key()
            else:
                address = list_ips[i - 1]
                pubKey = client.send_msg("whats_your_pub_key", str(address.split(":")[0]),
                                         int(address.split(":")[1])).decode("utf-8")
                # pubKey = client.ask_for_pub(str(address.split(":")[0]), int(address.split(":")[1]))

            print("interesting")
            if i == len(list_ips) - 1:
                print("sadkfjsdfkj")
                print(address)
                encrMsg = client.cypherClient.encrypt(msg, pubKey)
            encryptedList.append(client.cypherClient.encrypt(list_ips[i], pubKey))

        encNetMsg = client.create_network_message(encrMsg, encryptedList)
        return encNetMsg

    # encryptedList = encrypt(list_of_nodes)
    print("encrypted:")
    encryptedNetworkMessage = encrypt(msgToSend, list_of_nodes)
    print(encryptedNetworkMessage)

    # exit(0)

    # client.send_msg("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbb", destHOST, destPORT)
    # msg = client.create_network_message("hello world! hows the weather?", ["192.168.1.40:10001"])
    msg = encryptedNetworkMessage
    client.send_msg(msg, nextHOST, nextPORT)



if __name__ == "__main__":
    client.run_server()
    app.run(debug=True)
    print("good")
