from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # 处理跨域请求

@app.route('/submit-data', methods=['POST'])
def submit_data():
    data = request.json  # 获取前端传输的 JSON 数据
    print("Received data from frontend:", data)  # 打印接收到的数据

    # 在这里可以对接收到的数据进行进一步处理
    response_data = {'message': 'Data received successfully'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
