import requests
from bs4 import BeautifulSoup

url = 'https://chat18.aichatos.xyz/#/chat/1709864298265'  # 替换成你要提取文本信息的网页链接

try:
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=5 ,verify=False)
    response.raise_for_status()  # 如果请求失败，会抛出异常
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # 提取网页上的所有文字内容
    text_content = soup.get_text()
    # 将提取到的文字内容写入到txt文件中
    with open('web_text.txt', 'w', encoding='utf-8') as file:
        file.write(text_content)
    print("网页上的文字内容已保存到web_text.txt文件中")
except requests.RequestException as e:
    print("请求失败:", e)
except IOError as e:
    print("文件写入失败:", e)
