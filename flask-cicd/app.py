from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Phạm Huy Hoàng 22DH114540"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
