from flask import Blueprint, render_template, jsonify
from sklearn.datasets import load_iris


knn_bp = Blueprint(
    'knn',
    __name__, # 幫助 Flask 找到模板 (template) 和靜態文件 (static) 的位置
    url_prefix='/knn', # 此 Blueprint 中所有路由的 URL 都會自動加上這個前綴
    template_folder='../templates', # 指定這個blueprint模板的資料夾
    static_folder='../static' # 指定這個blueprint靜態文件的資料夾
)

@knn_bp.route('/knn_index')
def knn_index():
    return render_template('knn.html')

@knn_bp.route('/api/data')
def knn_data():
    '''knn 分類 API - 使用鳶尾花資料集'''
    iris = load_iris()
    print(iris)
    return jsonify(
        {
            "success": True
        }
    )