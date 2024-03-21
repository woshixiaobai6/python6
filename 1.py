from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os

app = Flask(__name__)
CORS(app)  # 处理跨域请求

@app.route('/submit-photo', methods=['POST'])
def submit_photo():
    data = request.get_json()
    
    if 'imageData' in data:
        image_data = data['imageData']
        print(f"Received image data: {image_data[:50]}")  # 打印前50个字符的图像数据，以便查看是否正确接收
        
        # 处理 base64 编码的图片数据
        try:
            image_data = image_data.split(',')[1]  # 去掉前缀部分
            image_data = base64.b64decode(image_data)
            
            # 保存图像数据到指定的目录 "D:\测试"
            target_directory = r'D:\测试'  # 指定保存文件的目录
            file_path = os.path.join(target_directory, 'image.jpg')
            with open(file_path, 'wb') as f:
                f.write(image_data)
                
            response_data = {'message': f'Photo submitted successfully and saved at: {file_path}'}
        except Exception as e:
            response_data = {'error': str(e)}
            print(f"An error occurred: {e}")
    else:
        response_data = {'error': 'No image data found'}
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)
