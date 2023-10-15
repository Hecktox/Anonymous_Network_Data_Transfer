from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

# A list to store added IPs
added_ips = []

@app.route('/')
def index():
    return render_template('Page1.html', added_ips=added_ips)

@app.route('/Page2')
def about():
    return render_template('Page2.html')

@app.route('/add_ip', methods=['POST'])
def add_ip():
    new_ip = request.form.get('newIP')
    if new_ip and new_ip.strip():
        added_ips.append(new_ip)
        update_node_file()
    return index()

@app.route('/send_message', methods=['POST'])
def send_message():
    new_ip = request.form.get('messageInput')
    if new_ip and new_ip.strip():
        added_ips.append(new_ip)
    return index()

def update_node_file():
    try:
        with open('list_of_nodes.txt', 'w+') as f:
            ip_string = ', '.join(added_ips)
            f.write(ip_string)
    except Exception as e:
        print("Error writing to file: {}".format(str(e)))

if __name__ == "__main__":
    app.run(debug=True)
