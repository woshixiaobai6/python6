import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# 设置抢票的时间
target_time = datetime.datetime(2024, 3, 11, 10, 50, 0)  # 设定抢购时间
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
time.sleep(3)
browser.implicitly_wait(10)  # 设置隐式等待时间
browser.maximize_window()  # 最大化浏览器窗口

# 登录
# login_link = WebDriverWait(browser, 50).until(EC.presence_of_element_located((By.LINK_TEXT, "亲，请登录")))
# login_link.click()

# 预留时间登录
time.sleep(10)
browser.get("https://cart.taobao.com/cart.htm")
time.sleep(3)

# 是否全选购物车
while True:
    try:
        if browser.find_element_by_id("J_SelectAll1"):
            browser.find_element_by_id("J_SelectAll1").click()
            break
    except:
        print("找不到购买按钮")

# 进入抢购流程
while True:
    # 获取当前时间
    now = datetime.datetime.now()
    
    # 对比时间，时间到的话就点击结算
    print(now)
    
    if now >= target_time:
        # 点击结算按钮
        while True:
            try:
                if browser.find_element_by_link_text("结 算"):
                    print("点击结算按钮")
                    browser.find_element_by_link_text("结 算").click()
                    print("结算成功")
                    break
            except:
                pass
        
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element_by_link_text('提交订单'):
                    browser.find_element_by_link_text('提交订单').click()
                    print("抢购成功，请尽快付款")
            except:
                print("抢购成功，请尽快付款")
                break
        time.sleep(0.01)
