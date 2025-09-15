from flask import Flask

app = Flask(__name__)
@app.route('/') #根目錄
def index():
    return '<h1 style="color:red">您好，Flask！</h1>'

@app.route("/name") #路由節點
def name():
    return '<h1>您好，Flask！</h1>'


if __name__ == "__main__":
    app.run(debug=True)