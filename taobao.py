import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 设置抢票的时间
target_time = datetime.datetime(2024, 3, 11, 14, 30, 0)  # 设定抢购时间

# 实例化 Chrome WebDriver
browser = webdriver.Chrome()
browser.implicitly_wait(10)  # 设置隐式等待时间
browser.maximize_window()  # 最大化浏览器窗口

# 打开淘宝网页并登录
browser.get("https://www.taobao.com")
wait = WebDriverWait(browser, 10)
login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "亲，请登录")))
login_link.click()

# 预留时间登录
# time.sleep(10)
# browser.get("https://cart.taobao.com/cart.htm")
# time.sleep(3)

# 是否全选购物车
while True:
    try:
        if browser.find_element(By.ID, "J_SelectAll1"):
            browser.find_element(By.ID, "J_SelectAll1").click()
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
                if browser.find_element(By.LINK_TEXT, "结 算"):
                    print("点击结算按钮")
                    browser.find_element(By.LINK_TEXT, "结 算").click()
                    print("结算成功")
                    break
            except:
                pass
        
        # 点击提交订单按钮
        while True:
            try:
                if browser.find_element(By.LINK_TEXT, '提交订单'):
                    browser.find_element(By.LINK_TEXT, '提交订单').click()
                    print("抢购成功，请尽快付款")
                    break
            except:
                print("抢购失败，继续尝试")
        
        # 抢购成功，退出循环
        break

# 关闭浏览器
browser.quit()
