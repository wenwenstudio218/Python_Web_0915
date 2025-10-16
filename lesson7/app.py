from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/regression")
def regression():
    return render_template("regression.html")

@app.route("/knn")
def knn():
    return render_template("knn.html")

@app.route("/test")
def test():
    return render_template("test.html")


def main():
    app.run(debug=True,port=5001)

if __name__ == "__main__":
    main()