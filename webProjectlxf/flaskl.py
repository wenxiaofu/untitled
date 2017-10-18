from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('signin.html')

@app.route('/signin', methods=['POST'])

def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='123456':

        return render_template('success.html',username=request.form['username'])
    else:
        return render_template('success.html',message='Bad username or password', username=\
            request.form['username'])

if __name__ == '__main__':
    app.run()