from flask import Flask,request

app = Flask(__name__)

@app.route('/index/')
def index():
    print(request.args)
    return 'successed'

if __name__ == '__main__':
    app.run()