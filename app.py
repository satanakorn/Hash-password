from flask import Flask, render_template, request
import bcrypt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return render_template('index.html', hashed_password=hashed_password.decode('utf-8'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
