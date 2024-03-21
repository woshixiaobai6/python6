import requests  # 导入requests库，用于发送HTTP请求
from lxml import etree  # 导入etree模块，用于解析HTML文档
import pandas as pd  # 导入pandas库，用于数据处理
import matplotlib.pyplot as plt  # 导入matplotlib库，用于数据可视化
from matplotlib.font_manager import FontProperties  # 导入FontProperties类，用于设置字体

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}
# 设置请求头，模拟浏览器发送请求的User-Agent

resp = requests.get('https://www.qb5.vip/top/allvisit/', headers=headers)
# 使用requests库发送GET请求，获取指定网页的内容

e = etree.HTML(resp.text)
# 使用etree.HTML()方法解析网页内容，得到一个可操作的XPath对象

types = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[1]/text()')
# 使用XPath语法提取网页中的书籍类型数据

names = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[2]/a/text()')
# 使用XPath语法提取网页中的书籍名称数据

authors = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[3]/text()')
# 使用XPath语法提取网页中的作者数据

counts = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[5]/text()')
# 使用XPath语法提取网页中的字数数据

nums = e.xpath('//div[@id="articlelist"]/ul[2]/li/span[6]/text()')
# 使用XPath语法提取网页中的推荐数数据

datas = []
# 创建一个空列表，用于存储提取到的数据

for t, name, author, count, num in zip(types, names, authors, counts, nums):
    # 使用zip()函数将多个列表按元素进行配对
    datas.append([t, name, author, count[:-1], num])
    # 将每个配对的数据以列表形式添加到datas列表中，
    # count[:-1]表示去掉count末尾的字符（单位）

df = pd.DataFrame(datas, columns=['类型', '书名', '作者', '字数', '推荐'])
# 使用pandas库将二维列表datas转换为DataFrame对象df，并为每一列命名

df['推荐'] = df['推荐'].astype('int')
# 将推荐列的数据类型转换为整型

df.describe()
# 使用describe()方法获取数据的统计描述信息

df.groupby('类型').count()
# 使用groupby()方法按照类型列进行分组，然后使用count()方法统计每个分组中的数量

#font_path = 'caisemenghuanjingyu.ttf'  # 替换为自定义字体文件的路径
# 设置自定义字体的路径

#custom_font = FontProperties(fname=font_path)
# 创建FontProperties对象，用于设置字体样式

df.类型.hist()
# 绘制类型列的直方图

#plt.xlabel('类型', fontproperties=custom_font)
# 设置x轴标签，并使用自定义字体

plt.show()
# 显示图形

df[df.类型 == '玄幻魔法'].sort_values(by='推荐')
# 对df进行筛选，只保留类型为'玄幻魔法'的行，并按照推荐列进行升序排序

df = pd.DataFrame(datas, columns=['类型', '书名', '作者', '字数', '推荐'])
# 重新将二维列表datas转换为DataFrame对象df，并为每一列命名

df.to_excel('data.xlsx', index=False)
# 将DataFrame保存为Excel文件，文件名为data.xlsx，不包含索引列

