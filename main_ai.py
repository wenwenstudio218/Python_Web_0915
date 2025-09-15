#todo:請建立一個Flask應用程式，並在根路由('/')上設置一個GET請求處理函數，該函數返回一個簡單的"Hello, World!"訊息。
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run(debug=True)