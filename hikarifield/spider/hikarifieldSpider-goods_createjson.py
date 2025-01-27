import os
import sys
import re
import json
import requests
from datetime import datetime
from bs4 import BeautifulSoup

# 打印欢迎消息和当前时间
print("欢迎运行hikarifield爬虫")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("当前时间:", current_time)

# 检测./goods_info.json文件是否存在
json_file = "../public/json/goods_info.json"
if os.path.exists(json_file):
    print("成功检测到目标文件，即将为您更新数据")
else:
    print("未检测到目标文件，正在为您下载最新模板")
    url = "https://github.com/SouthernDreamS6/homepage/raw/main/hikarifield/public/json/goods_info.json"
    try:
        #尝试向指定的URL发送GET请求
        response = requests.get(url)
        #检查响应状态码
        response.raise_for_status()

        with open(json_file, "wb") as file:
            file.write(response.content)
        
        print("模板文件下载完成，重新运行脚本以继续")
        sys.exit(0)
    
    except requests.RequestException as e:
        print(f"无法下载模板文件: {e}")
        sys.exit(1)

# 读取./goods_info.json中每个数组的第一条数据作为变量用于后续数据对比
with open(json_file, "r", encoding="utf-8") as file:
    json_file_data = json.load(file)

# 读取cookie.txt文件中的cookie
with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie = f.read().strip()

# 设置请求头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.360',
    'Cookie': cookie,
    'Referer': 'https://store.hikarifield.co.jp/full_games'
}

base_url = "https://store.hikarifield.co.jp/goods/"


# 爬取站点数据并与./goods_info.json变量中的对应数据做对比
for product_id in range(1, 161):

    url = f"{base_url}{product_id}"
    
    try:
        # 发起请求
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        # 解析页面
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 判断商品ID是否存在
        error_page = soup.find("div", class_="error-page px-4")
        if error_page:
            print(f"商品ID {product_id} 不存在或未上架，跳过")
            continue
        
        # 检查 JSON 文件中是否存在对应 ID 的商品
        existing_item = next((item for item in json_file_data if item["id"] == str(product_id)), None)
        
        if not existing_item:
            # 如果不存在，创建新的商品对象并添加到 JSON 数据中
            new_item = {
                "workName": "",
                "id": str(product_id),
                "goodsName": "",
                "prices": {
                    "now": [
                        {
                        "date": "1999.01.01",
                        "price": 999
                        }
                    ],
                    "scNow": [
                        {
                        "date": "1999.01.01",
                        "price": 999
                        }
                    ],
                    "low": [
                        {
                        "date": "1999.01.01",
                        "price": 999
                        }
                    ],
                    "old": [
                        {
                        "date": "1999.01.01",
                        "price": 999
                        }
                    ]
                },
                "imgUrl": "",
                "salesTime": ""
            }
            json_file_data.append(new_item)
            existing_item = new_item  # 指向新创建的对象
            print(f"商品ID {product_id} 不存在于 JSON 文件中，已创建新记录")

    except requests.RequestException as e:
        print(f"请求商品ID {product_id} 时出错: {e}")
    except Exception as e:
        print(f"处理商品ID {product_id} 时出错: {e}")

# 保存更新后的 JSON 数据
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(json_file_data, file, ensure_ascii=False, indent=2)
    print("数据更新已保存")