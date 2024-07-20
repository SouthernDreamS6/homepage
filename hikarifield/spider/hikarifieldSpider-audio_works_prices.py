#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本名称: hikarifield爬虫脚本——音声作品
版本: 1.0
作者: 南梦故间
日期: 2024-07-20
描述: 该脚本用于从hikarifield网站爬取产品价格信息并更新audio_works_prices.json文件。
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

# 检测./audio_works_prices.json文件是否存在
json_file = "../public/json/audio_works_prices.json"
if os.path.exists(json_file):
    print("成功检测到目标文件，即将为您更新数据")
else:
    print("未检测到目标文件，正在为您下载最新模板")
    url = "https://github.com/SouthernDreamS6/homepage/raw/main/hikarifield/public/json/audio_works_prices.json"
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

# 读取./audio_works_prices.json中每个数组的第一条数据作为变量用于后续数据对比
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

base_url = "https://store.hikarifield.co.jp/shop/"

product_ids = [
    "ayakashi_sumi",
    "ayakashi_nana",
    "ayakashi_natsu",
    "ayakashi_alice",
    "ayakashi_hime",
    "chikuon_rail_beni",
    "chikuon_rail_kiko",
    "chikuon_rail_suika",
    "chikuon_rail_suzushiro",
    "chikuon_rail_kaniko",
    "chikuon_rail_ran"
]

# 爬取站点数据并与./audio_works_prices.json变量中的对应数据做对比
for product_id in product_ids:
    

    jsonPrices = {
        "now": next((int(entry["prices"]["now"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "old": next((int(entry["prices"]["old"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "gift": next((int(entry["prices"]["gift"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "scNow": next((int(entry["prices"]["scNow"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None)
    }
    url = f"{base_url}{product_id}"
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        # 解析产品信息
        product_info = {
            "id": product_id,
            "name": "N/A",
            "prices": {
                "now": [],
                "old": [],
                "gift": [],
                "scNow": []
            }
        }
        
        print(f"正在爬取 {product_id}")
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
        
        # 获取礼物价
        label_tags = soup.find_all("label", class_="form-check-label")
        if label_tags:
            second_label_tag = label_tags[1]
            small_tag = second_label_tag.find("small")
            if small_tag:
                small_text = small_tag.get_text(strip=True)
                giftPrice_match = re.search(r'（(\d+)元）', small_text)
                if giftPrice_match:
                    giftPrice = int(giftPrice_match.group(1))
                    new_gift_price_data = {
                        "date": datetime.now().strftime("%Y.%m.%d"),
                        "price": giftPrice
                    }
                    
                    # 检查是否需要插入新数据
                    if jsonPrices["gift"] != giftPrice:
                        product_info["prices"]["gift"].append(new_gift_price_data)
                        print("gift原数据", jsonPrices["gift"]) 
                        print("数据变动", giftPrice) 
        
        # 获取scNow价格
        discount_list = soup.find("ul", class_="discount-list")
        if discount_list:
            li_tags = discount_list.find_all("li")
            for li in li_tags:
                if "SLAM CARD" in li.get_text():
                    sc_now_tag = li.find("span", class_="price")
                    if sc_now_tag:
                        sc_now_price_text = sc_now_tag.get_text(separator=" ", strip=True)
                        sc_now_price = int(re.search(r'\d+', sc_now_price_text).group())
                        new_sc_now_data = {
                            "date": datetime.now().strftime("%Y.%m.%d"),
                            "price": sc_now_price
                        } 

                        # 检查是否需要插入新数据
                        if jsonPrices["scNow"] != sc_now_price:
                            product_info["prices"]["scNow"].append(new_sc_now_data)
                            print("scNow原数据", jsonPrices["scNow"]) 
                            print("数据变动", sc_now_price) 

        # 更新./audio_works_prices.json文件中对应数组
        for existing_entry in json_file_data:
            if existing_entry["id"] == product_id:
                existing_entry["prices"]["now"] = product_info["prices"]["now"] + existing_entry["prices"]["now"]
                existing_entry["prices"]["old"] = product_info["prices"]["old"] + existing_entry["prices"]["old"]
                existing_entry["prices"]["gift"] = product_info["prices"]["gift"] + existing_entry["prices"]["gift"]
                existing_entry["prices"]["scNow"] = product_info["prices"]["scNow"] + existing_entry["prices"]["scNow"]
                break
    
    except requests.RequestException as e:
        print(f"Error fetching data for product ID {product_id}: {e}")

# 保存更新后的JSON数据
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(json_file_data, file, ensure_ascii=False, indent=2)

print("数据已更新至 audio_works_prices.json 文件中")
