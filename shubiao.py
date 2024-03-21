import pyautogui
import time

# 录制鼠标操作
print('开始录制鼠标操作，按Ctrl+C停止...')
actions = []
try:
    while True:
        x, y = pyautogui.position()
        actions.append((x, y))
        print(f'pyautogui.moveTo({x}, {y})')
        time.sleep(0.5)  # 增加延迟时间
except KeyboardInterrupt:
    pass

# 重复执行鼠标操作
print('开始执行鼠标操作，按Ctrl+C停止...')
try:
    while True:
        for action in actions:
            pyautogui.moveTo(action[0], action[1])
            time.sleep(0.01)  # 增加延迟时间
except KeyboardInterrupt:
    pass
