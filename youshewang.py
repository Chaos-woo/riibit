import datetime
import os
import random
import urllib.parse
import re

import requests
from bs4 import BeautifulSoup


def fetch_youshewang():
    app = '优设网'

    # 设置请求头，模拟浏览器访问
    ip = generate_random_public_ip()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
        'CLIENT-IP': ip,
        'X-FORWARDED-FOR': ip,
        'Referer': 'https://www.uisdc.com',
    }

    # 热搜地址
    url = 'https://www.uisdc.com/archives'

    # 发送请求
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'

    # 检查请求是否成功
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有文章列表项
        list_dom = soup.find_all('h2', attrs={'class': 'item-title'})

        # 提取列表数据
        list_data = []
        for item in list_dom:
            # 提取信息
            a = item.find('a')
            url = a.get('href') if a else None
            title = a.get_text(strip=True) if a else ''

            # 构建移动端URL
            hot_search_url = url

            if title == '' or url == None:
                continue

            # 将数据添加到列表
            list_data.append({
                'title': title,
                'url': hot_search_url
            })

        hot_searches = list_data
        year = datetime.datetime.now().strftime('%Y')
        month = datetime.datetime.now().strftime('%m')
        formatted_month = str(month).zfill(2)
        parent_file_path = f'./archives/{app}/{year}/{formatted_month}'
        # 确保目录存在
        if not os.path.exists(parent_file_path):
            os.makedirs(parent_file_path, exist_ok=True)

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        file_path = f'./archives/{app}/{year}/{formatted_month}/{current_date}.md'

        # 读取文件内容，检查是否已经存在
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                existing_content = file.read()
        else:
            existing_content = ''

        # 本次内容去重
        markdown_links = []
        for item in hot_searches:
            # 构建超链接文本和链接
            link_text = item['title']
            encoded_link = urllib.parse.quote(link_text)
            link = item['url']

            # 构建markdown格式的超链接
            markdown_link = f'+ [{link_text}]({link})\n'
            if markdown_link not in markdown_links:
                markdown_links.append(markdown_link)

        # 写入内容
        with open(file_path, 'a', encoding='utf-8') as file:
            for item in markdown_links:
                # 构建markdown格式的超链接
                markdown_link = item

                # 检查内容是否已经存在
                if markdown_link not in existing_content:
                    file.write(markdown_link)

    else:
        print('Failed to retrieve data')


def generate_random_public_ip():
    # 生成第一个数字，1-223之间，避免使用127（本地回环）和0（默认保留）
    first_octet = random.choice([str(num) for num in range(1, 224) if num not in [127, 0]])

    # 生成第二个数字，0-254之间
    second_octet = str(random.randint(0, 254))

    # 生成第三个数字，0-254之间
    third_octet = str(random.randint(0, 254))

    # 生成第四个数字，1-254之间，避免使用0（网络地址）和255（广播地址）
    fourth_octet = str(random.randint(1, 254))

    return '.'.join([first_octet, second_octet, third_octet, fourth_octet])

def get_numbers(url):
    # 这个函数需要根据实际的getNumbers函数实现来提取URL中的数字
    # 这里假设它提取URL中最后一个斜杠 '/' 后面的数字
    import re
    match = re.search(r'/(\d+)/', url)
    return match.group(1) if match else None
