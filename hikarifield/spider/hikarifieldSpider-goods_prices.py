#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本名称: hikarifield爬虫脚本——实物周边（测试中）
版本: 0.1
作者: 南梦故间
日期: 2024-07-20
描述: 该脚本用于从hikarifield网站爬取产品价格信息并更新goods_info.json文件。
用法：使用前请先抓取hikarifield账号cookie并储存于脚本目录下的cookie.txt文件中。
"""
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
        response = requests.get(url)
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
for product_id in range(1, 61):

    jsonPrices = {
        "now": next((int(entry["prices"]["now"][0]["price"]) for entry in json_file_data if entry["id"] == str(product_id)), None),
        "scNow": next((int(entry["prices"]["scNow"][0]["price"]) for entry in json_file_data if entry["id"] == str(product_id)), None),
        "old": next((int(entry["prices"]["old"][0]["price"]) for entry in json_file_data if entry["id"] == str(product_id)), None),
        "stockStatus": next((entry["stockStatus"] for entry in json_file_data if entry["id"] == str(product_id)), None)
    }
    url = f"{base_url}{product_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 判断商品ID是否存在
        error_page = soup.find("div", class_="error-page px-4")
        if error_page:
            print(f"商品ID {product_id} 不存在或未上架，跳过")
            continue

        # 解析产品信息
        product_info = {
            "id": str(product_id),
            "goodsName": "N/A",
            "prices": {
                "now": [],
                "scNow": [],
                "old": []
            },
            "stockStatus": "N/A",
            "imgUrl": "N/A"
        }
        
        print(f"正在爬取 {product_id}")
        
        # 获取商品名称和库存状态
        title_tag = soup.find("div", class_="title mt-2")
        if title_tag:
            # 获取商品名称和库存状态
            goods_name_with_status = title_tag.get_text(separator=" ", strip=True)
            stock_status_tag = title_tag.find("span", class_="badge presale bg-success")
            
            # 如果找不到特定的类组合，再尝试查找通用的 "badge" 类
            if not stock_status_tag:
                stock_status_tag = title_tag.find("span", class_="badge")
            
            stock_status = stock_status_tag.get_text(strip=True) if stock_status_tag else "N/A"
            
            # 商品名称可能在前面，库存状态可能在后面，这里假设库存状态标签存在并且出现在名称后面
            if stock_status != "N/A":
                goods_name = goods_name_with_status.replace(stock_status, "").strip()
            else:
                # 如果库存状态标签不存在，只获取商品名称
                goods_name = goods_name_with_status
            
            product_info["goodsName"] = goods_name
            print("商品名称:", goods_name)
            print("库存状态:", stock_status)
    
            
            # 检查是否需要插入新数据
            if jsonPrices["stockStatus"] != stock_status:
                product_info["stockStatus"] = stock_status
                print("stockStatus原数据:", jsonPrices["stockStatus"])
                print("数据变动:", stock_status)
        
        # 获取当前价格
        discount_price_tag = soup.find("span", class_="discount-price")
        if discount_price_tag:
            discount_price_text = discount_price_tag.get_text(separator=" ", strip=True)
            product_price = int(re.search(r'\d+', discount_price_text).group())
            new_price_data = {
                "date": datetime.now().strftime("%Y.%m.%d"),
                "price": product_price
            }
            
            # 检查是否需要插入新数据
            if jsonPrices["now"] != product_price:
                product_info["prices"]["now"].append(new_price_data)
                print("now原数据", jsonPrices["now"]) 
                print("数据变动", product_price) 
        
        # 获取原价
        original_price_tag = soup.find("span", class_="original-price")
        if original_price_tag:
            original_price_text = original_price_tag.get_text(separator=" ", strip=True)
            old_price = int(re.search(r'\d+', original_price_text).group())
            new_old_price_data = {
                "date": datetime.now().strftime("%Y.%m.%d"),
                "price": old_price
            }
            
            # 检查是否需要插入新数据
            if jsonPrices["old"] != old_price:
                product_info["prices"]["old"].append(new_old_price_data)
                print("old原数据", jsonPrices["old"]) 
                print("数据变动", old_price) 

        # 获取SLAM CARD价格
        discount_details = soup.find("div", class_="discount-details mt-2")
        if discount_details:
            li_tags = discount_details.find_all("li")
            for li_tag in li_tags:
                if "SLAM CARD" in li_tag.get_text():
                    sc_price_text = li_tag.find("strong", class_="text-danger").get_text(strip=True)
                    sc_price = int(re.search(r'\d+', sc_price_text).group())
                    new_sc_price_data = {
                        "date": datetime.now().strftime("%Y.%m.%d"),
                        "price": sc_price
                    }
            
                    # 检查是否需要插入新数据
                    if jsonPrices["scNow"] != sc_price:
                        product_info["prices"]["scNow"].append(new_sc_price_data)
                        print("scNow原数据", jsonPrices["scNow"]) 
                        print("数据变动", sc_price) 
        
        # 获取图片URL
        link_tag = soup.find("a", class_="link", href=True)
        if link_tag:
            img_url = re.search(r'goods/(.*)', link_tag['href']).group(1)
            product_info["imgUrl"] = img_url
        
        # 更新./goods_info.json文件中对应数组
        for existing_entry in json_file_data:
            if existing_entry["id"] == str(product_id):
                existing_entry["prices"]["now"] = product_info["prices"]["now"] + existing_entry["prices"]["now"]
                existing_entry["prices"]["scNow"] = product_info["prices"]["scNow"] + existing_entry["prices"]["scNow"]
                existing_entry["prices"]["old"] = product_info["prices"]["old"] + existing_entry["prices"]["old"]
                existing_entry["goodsName"] = product_info["goodsName"]
                existing_entry["stockStatus"] = product_info["stockStatus"]
                existing_entry["imgUrl"] = product_info["imgUrl"]
                break
    
    except requests.RequestException as e:
        print(f"Error fetching data for product ID {product_id}: {e}")

# 保存更新后的JSON数据
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(json_file_data, file, ensure_ascii=False, indent=2)

print("数据已更新至 goods_info.json 文件中")