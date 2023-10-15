from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('Page1.html')

@app.route('/about')
def about():
    return render_template('Page2.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    if request.method == 'POST':
        ip_list = request.form.getlist('ip_address')
        # Process the list of IP addresses as needed
        print(ip_list)  # Example: Printing the list of IP addresses
        return 'IP addresses received successfully'



if __name__ == "__main__":
    app.run()