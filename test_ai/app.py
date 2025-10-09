from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/machine")
def machine():
    return render_template("machine.html")

def main():
    app.run(debug=True,port=5001)

if __name__ == "__main__":
    main()