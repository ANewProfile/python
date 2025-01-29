from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    return f'Username: {username}, Password: {password}'


if __name__ == '__main__':
    app.run(debug=True)
