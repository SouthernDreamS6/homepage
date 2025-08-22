#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本名称: hikarifield爬虫脚本——视觉小说
版本: 1.0
作者: 南梦故间
日期: 2024-07-20
描述: 该脚本用于从hikarifield网站爬取产品价格信息并更新galgames_prices.json文件。
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

# 检测./galgames_prices.json文件是否存在
json_file = "../public/json/galgames_prices.json"
if os.path.exists(json_file):
    print("成功检测到目标文件，即将为您更新数据")
else:
    print("未检测到目标文件，正在为您下载最新模板")
    url = "https://github.com/SouthernDreamS6/homepage/raw/main/hikarifield/public/json/galgames_prices.json"
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

# 读取./galgames_prices.json中每个数组的第一条数据作为变量用于后续数据对比
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
    "tayutama2", 
    "sakura_no_mori", 
    "monobeno",
    "monobeno_happy_end",
    "hello_lady",
    "maitetsu_pure_station",
    "sakura_no_mori2",
    "hello_lady_nd",
    "tsukikage",
    "aokana",
    "alias_carnival",
    "natsunoiro",
    "senren_banka",
    "tryment_alpha",
    "happiness2",
    "maitetsu_lastrun",
    "aokana_extra1",
    "riddle_joker",
    "relief",
    "kinkoi",
    "parquet",
    "honoguraki",
    "hello_lady_se",
    "madoki",
    "sekachu",
    "stella",
    "hananono",
    "magical_charming",
    "tsukiniyorisou",
    "kinkoigt",
    "yumahorome",
    "cross_concerto",
    "soratoto",
    "aonatsu",
    "aokana_extra2",
    "future_radio",
    "shuffle_ep2",
    "witch_garden",
    "alias_carnival_flowering_sky",
    "sothewitch",
    "koikake",
    "clover_days",
    "arcana",
    "otomeriron",
    "seikano",
    "making_lovers",
    "sorechiru",
    "parfait_remake",
    "haruyome",
    "hitme",
    "kakenuke",
    "selectoblige",
    "hatuyuki",
    "tenshisouzou",
    "kirakano",
	"koichoco",
	"tsukiniyorisou_2nd",
	"sickly_days",
    "aozora_refine"
]

# 爬取站点数据并与./galgames_prices.json变量中的对应数据做对比
for product_id in product_ids:
    

    jsonPrices = {
        "now": next((int(entry["prices"]["now"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "low": next((int(entry["prices"]["low"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "old": next((int(entry["prices"]["old"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None),
        "gift": next((int(entry["prices"]["gift"][0]["price"]) for entry in json_file_data if entry["id"] == product_id), None)
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
                "low": [],
                "old": [],
                "gift": []
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
            
             # 新增的low数据对比
            if jsonPrices["low"] is None or jsonPrices["low"] > product_price:
                product_info["prices"]["low"].append(new_price_data)
                print("low原数据", jsonPrices["low"]) 
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
        
        # 更新./galgames_prices.json文件中对应数组
        for existing_entry in json_file_data:
            if existing_entry["id"] == product_id:
                existing_entry["prices"]["now"] = product_info["prices"]["now"] + existing_entry["prices"]["now"]
                existing_entry["prices"]["low"] = product_info["prices"]["low"] + existing_entry["prices"]["low"]
                existing_entry["prices"]["old"] = product_info["prices"]["old"] + existing_entry["prices"]["old"]
                existing_entry["prices"]["gift"] = product_info["prices"]["gift"] + existing_entry["prices"]["gift"]
                break
    
    except requests.RequestException as e:
        print(f"Error fetching data for product ID {product_id}: {e}")

# 保存更新后的JSON数据
with open(json_file, "w", encoding="utf-8") as file:
    json.dump(json_file_data, file, ensure_ascii=False, indent=2)

print("数据已更新至 galgames_prices.json 文件中")
