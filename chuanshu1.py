from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)
CORS(app)  # 处理跨域请求

def send_email(receiver_email, file_path):
    sender_email = '1543807401@qq.com'
    sender_password = 'kzvygetazsaqijfj'

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = 'Photo Submission'

    body = 'Please find the attached photo.'
    msg.attach(MIMEText(body, 'plain'))

    attachment = open(file_path, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(file_path))
    msg.attach(part)

    server = smtplib.SMTP_SSL('smtp.qq.com', 465)
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

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
                
            receiver_email = '1543807401@qq.com'  # 收件人 QQ 邮箱
            send_email(receiver_email, file_path)  # 发送邮件

            os.remove(file_path)  # 删除文件

            response_data = {'message': f'Photo submitted successfully and sent to {receiver_email}'}
        except Exception as e:
            response_data = {'error': str(e)}
            print(f"An error occurred: {e}")
    else:
        response_data = {'error': 'No image data found'}
    
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='192.168.161.97', debug=True)
