import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# 调用摄像头录制视频
def record_video():
    try:
        camera = cv2.VideoCapture(0)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

        while(camera.isOpened()):
            ret, frame = camera.read()
            if ret==True:
                out.write(frame)
                cv2.imshow('frame',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        camera.release()
        out.release()
        cv2.destroyAllWindows()

        # 新添加：释放视频文件，确保资源被正确释放
        del(camera)
        del(out)

        return 'output.avi'
    except Exception as e:
        print("发生异常:", e)
        camera.release()
        out.release()
        cv2.destroyAllWindows()

# 发送邮件
def send_email(video_path):
    from_addr = '1543807401@qq.com'
    to_addr = '1543807401@qq.com'
    password = 'kzvygetazsaqijfj'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = '录制的视频'

    # 添加视频附件
    if os.path.exists(video_path):
        attachment = open(video_path, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % os.path.basename(video_path))
        msg.attach(part)
    else:
        print('视频文件不存在')

    try:
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())
        server.quit()
        print('邮件发送成功')

        # 邮件发送成功后，删除本地视频文件
        if os.path.exists(video_path):
            os.remove(video_path)
            print('本地视频文件已删除')
        else:
            print('本地视频文件不存在')
    except Exception as e:
        print('邮件发送失败', e)

# 调用录制视频函数并发送邮件
video_path = record_video()
if video_path:
    send_email(video_path)
print("视频录制并邮件发送完成")
