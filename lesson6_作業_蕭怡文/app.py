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

@app.route("/decision_tree")
def decision_tree():
    tree_info = {
        "algorithm": "決策樹分類器",
        "applications": ["垃圾郵件分類", "客戶流失預測", "疾病診斷"],
        "pros": ["容易理解", "不需要特徵縮放", "可視化清晰"]
    }
    return render_template("decision_tree.html", tree_info=tree_info)

@app.route("/lesson6_1")
def lesson6_1():
    page_title = "cindy的首頁"
    users = [
        {"name":"小明","is_vip":True},
        {"name":"小華","is_vip":True},
        {"name":"小王","is_vip":False}
    ]
    return render_template("lesson6_1.html",title = page_title,user_list = users)

def main():
    app.run(debug=True,port=5001)

if __name__ == "__main__":
    main()