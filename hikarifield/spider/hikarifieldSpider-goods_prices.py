#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
脚本名称: hikarifield爬虫脚本——实物周边（测试中）
版本: Ver 0.3
作者: 南梦故间
日期: 2025-05-09
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

# 读取JSON数据
with open(json_file, "r", encoding="utf-8") as file:
    json_file_data = json.load(file)

# 读取cookie
with open('cookie.txt', 'r', encoding='utf-8') as f:
    cookie = f.read().strip()

# 请求头配置
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Cookie': cookie,
    'Referer': 'https://store.hikarifield.co.jp/full_games'
}

base_url = "https://store.hikarifield.co.jp/goods/"

# 价格解析函数
def parse_price(text):
    match = re.search(r'(\d+)', text.replace(',', ''))  # 支持处理带逗号的数字
    return int(match.group(1)) if match else None

# 主爬虫逻辑
for product_id in range(1, 141):
    product_info = {
        "id": str(product_id),
        "goodsName": "N/A",
        "prices": {"now": [], "scNow": [], "old": []},
        "imgUrl": "N/A"
    }
    
    # 从JSON获取历史价格
    existing_entry = next((x for x in json_file_data if x["id"] == str(product_id)), None)
    jsonPrices = {
        "now": existing_entry["prices"]["now"][0]["price"] if existing_entry and existing_entry["prices"]["now"] else None,
        "scNow": existing_entry["prices"]["scNow"][0]["price"] if existing_entry and existing_entry["prices"]["scNow"] else None,
        "old": existing_entry["prices"]["old"][0]["price"] if existing_entry and existing_entry["prices"]["old"] else None
    } if existing_entry else {"now": None, "scNow": None, "old": None}

    url = f"{base_url}{product_id}"
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # 检查商品是否存在
        if soup.find("div", class_="error-page"):
            print(f"商品ID {product_id} 不存在，跳过")
            continue

        print(f"\n正在处理商品 {product_id}/160")

        # 解析商品名称
        title_tag = soup.find("div", class_="title mt-2")
        if title_tag:
            goods_name = title_tag.get_text(separator=" ", strip=True)
            product_info["goodsName"] = re.sub(r'\s+', ' ', goods_name).strip()
            print(f"商品名称: {product_info['goodsName']}")

        # 解析当前价格
        discount_price_tag = soup.find("span", class_="discount-price")
        if discount_price_tag:
            current_price = parse_price(discount_price_tag.get_text())
            if current_price and current_price != jsonPrices["now"]:
                product_info["prices"]["now"].append({
                    "date": datetime.now().strftime("%Y.%m.%d"),
                    "price": current_price
                })
                print(f"当前价格变动: {jsonPrices['now']} → {current_price}")

        # 解析原价
        original_price_tag = soup.find("span", class_="original-price")
        if original_price_tag:
            old_price = parse_price(original_price_tag.get_text())
            if old_price and old_price != jsonPrices["old"]:
                product_info["prices"]["old"].append({
                    "date": datetime.now().strftime("%Y.%m.%d"),
                    "price": old_price
                })
                print(f"原价变动: {jsonPrices['old']} → {old_price}")

        # 优化后的SLAM CARD价格解析
        discount_details = soup.find("div", class_="discount-details mt-2")
        sc_price = None
        
        if discount_details:
            # 使用CSS选择器精准定位包含SLAM CARD的条目
            slamcard_li = discount_details.select('li:has(a[href*="slam_cards"])')
            
            for li in slamcard_li:
                # 获取所有价格元素，取最后一个包含数字的
                price_elements = li.find_all("strong", class_="text-danger")
                for elem in reversed(price_elements):
                    price = parse_price(elem.get_text(strip=True))
                    if price:
                        sc_price = price
                        break
                if sc_price:
                    break

        if sc_price:
            if sc_price != jsonPrices["scNow"]:
                product_info["prices"]["scNow"].append({
                    "date": datetime.now().strftime("%Y.%m.%d"),
                    "price": sc_price
                })
                print(f"SC价格变动: {jsonPrices['scNow']} → {sc_price}")
        else:
            print(f"商品ID {product_id} 未找到SLAM CARD价格")

        # 解析图片URL
        link_tag = soup.find("a", class_="link", href=True)
        if link_tag:
            product_info["imgUrl"] = re.search(r'goods/(.*)', link_tag['href']).group(1)
            
            print(f"图片地址: {product_info['imgUrl']}")

        # 更新JSON数据
        if existing_entry:
            # 保留历史数据，只追加新变动
            for price_type in ["now", "scNow", "old"]:
                if product_info["prices"][price_type]:
                    existing_entry["prices"][price_type].insert(0, product_info["prices"][price_type][0])
                    existing_entry["goodsName"] = product_info["goodsName"]
                    existing_entry["imgUrl"] = product_info["imgUrl"]
        else:
            json_file_data.append(product_info)

    except Exception as e:
        print(f"处理商品 {product_id} 时发生错误: {str(e)}")
        continue

# 保存更新后的数据
try:
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(json_file_data, file, ensure_ascii=False, indent=2)
    print("\n数据更新完成！")
except Exception as e:
    print(f"保存文件失败: {str(e)}")
    sys.exit(1)