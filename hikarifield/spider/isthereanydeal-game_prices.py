import requests
import json
import os

# 从文件中读取 API key
with open('isthereanydeal_api_key.txt', 'r', encoding='utf-8') as file:
    api_key = file.read().strip()

# API 请求的基础 URL
url = f"https://api.isthereanydeal.com/games/prices/v3?key={api_key}&country="

# 游戏 ID 列表
game_ids = [
    "018d95d5-0c57-7238-aae3-a1a703799af2", # 游魂2-you're the only one-
    "018d937f-1c43-720c-b6a3-556e196f8f85", # 樱之杜†净梦者
    "018d937f-0c4d-71ff-8adc-6a1befa69240", # 茂伸奇谈-Monobeno-
    "018d937f-35ca-7030-82ff-d091b46c5ba0", # 茂伸奇谈-Happy End-
    "018d937f-2e97-71e8-a6e6-0eaa11d5c3be", # 淑女同萌！
    "018d937f-464f-73c6-8572-9af419a6f1a2", # 爱上火车-Pure Station-
    "018d937f-20dc-73eb-bf05-13ffb3cbf18a", # 樱之杜†净梦者2
    "018d937f-39b0-73b2-be1e-4692133699ee", # 淑女同萌！-New Division-
    "018d937f-3864-73b0-977a-6c1ec9471821", # 月影魅像-解放之羽-
    "018d937e-fa57-7217-8f92-74a1846666d1", # 苍之彼方的四重奏
    "018d937f-3a75-7176-a0a2-5efa419ada14", # 爱丽娅的明日盛典！（ALIA's Carnival!）
    "018d937f-3ab9-7169-92c6-794c2cea243b", # 追忆夏色年华
    "018d937f-3d3b-708a-8a70-7af2b44a4da4", # 千恋＊万花
    "018d96d1-bf16-7032-8016-efa7ee737581", # TrymenT ―献给渴望改变的你― Alpha篇
    "018d937f-4818-71e9-8370-c6b5862bb3da", # 爱上火车-Last Run!!-
    "018d937f-47ef-71b4-a8e5-417c8de870a6", # 苍之彼方的四重奏 EXTRA1
    "018d937f-4873-73e9-aabf-ee3adca536b7", # Riddle Joker
    "018d937f-4b3e-717a-9733-34e6ed82a18c", # Re:LieF 〜献给亲爱的你〜 Re:LanguagE
    "018d937f-50e7-7282-9f1a-d70b18bea507", # 金辉恋曲四重奏
    "018d937f-554d-72d8-8a28-5cdc6b0093eb", # PARQUET
    "018d937f-5c6d-731a-874b-a2e11597f983", # 淑女同萌！-Superior Entelecheia-
    "018d937f-5ccc-71ac-aad6-69106a5bf4f3", # 雪境迷途遇仙踪
    "018d937f-5ce5-706f-9424-bf8768bd7747", # 在世界与世界的正中央
    "018d937f-60b8-709f-862c-09b2087b9653", # 星光咖啡馆与死神之蝶
    "018d97ae-3bde-72e5-b87c-fd7ed7baa090", # 五色浮影绽放于花之海洋
    "018d979d-5f7d-73aa-a0c9-3ad821f31476", # 近月少女的礼仪
    "018d937f-6322-72d8-b8e5-4e5734d1c16a", # 金辉恋曲四重奏 -Golden Time-
    "018d937f-639e-7391-bb98-9285de62c502", # 真愿朦幻馆～在时间暂停的洋馆里追寻明天的羔羊们～
     # 交汇协奏曲
    "018d937f-6682-71dc-bed7-5b01d0c05557", # 天空的蓝与白/如梭夏日
    "018d97d6-e38a-73f3-8c81-6ceb69339818", # 青夏轨迹
    "018d937f-67cd-71d1-86ad-b9aa421d443f", # 苍之彼方的四重奏 EXTRA2
    "018d937f-6b41-72e7-b293-f8925107c8f2", # 未来广播与人工鸽
    "018d937f-6ba6-71f3-a6f7-6dc73dcb9c18", # SHUFFLE! episode2 ～被神与魔同时盯上的男人～
    "018d937f-6ca1-7197-906e-72060369ee8e", # 魔女的花园
    "018d937f-6fbc-724f-b275-a3c84e3ca581", # 爱丽娅的明日盛典！Flowering Sky
    "018d937f-733c-7065-a6e7-0fc0877134de", # 魔女的夜宴
    "018d937f-7396-724a-87ba-7f7ef4e3d79d", # 想要传达给你的爱恋
    "018d937f-744f-7085-a254-98b3be490b92", # 幸运草的约定 Clover Days
    "018d937f-7439-731c-b89f-29d3ac1bef73", # 炼爱秘仪
    "018d937f-79ee-7118-ba36-f9091aadd010", # 少女理论及其周边
    "018d937f-7a26-717c-9e0c-bb0e3d7b8c4a", # 制服女友
    "018ef5da-9617-7379-b173-bbbb31138c3a", # 突然＊恋人（Making＊Lovers）全高清合集版
    "018ff232-1fb7-72fe-8414-ac0311e3db95", # 繁花落舞恋如樱-Re:BIRTH-
    "0191c57d-9f4f-73b3-a205-9d0e07a027d5", # 纯爱咖啡厅~帕露菲重制版~
    "01905e5a-2756-73ee-bebe-a60b5b3e59de", # 献给蔚蓝之海的新娘
    "0191eae1-6343-7301-add5-720d83f151fb", # 你的眼眸命中我心头
    "01920ef0-7057-73fa-97be-194fc9ea70f0", # 绽放★青春全力向前冲！
    "0190ee88-1b12-71c1-8a1e-2b5734b56c86" # 天选庶民的真命之选
]

# 从文本文件中读取游戏 ID 列表
# game_ids = []
# with open('isthereanydeal-game_ids.txt', 'r') as file:
#     game_ids = [line.strip() for line in file.readlines() if line.strip()]

# 查询的国家列表，使用 ISO 3166-1 alpha-2 格式的国家代码
# 参考https://zh.wikipedia.org/wiki/ISO_3166-1%E4%BA%8C%E4%BD%8D%E5%AD%97%E6%AF%8D%E4%BB%A3%E7%A0%81
countries = [
#    "CN",   # 中国
#    "HK",   # 香港
#    "MO",   # 澳门
#    "TW",   # 台湾
#    "US",   # 美国
#    "RU",   # 俄罗斯
#    "UA",   # 乌克兰
#    "ZA"    # 南非
#    "AR",   # 阿根廷
#    "TR",   # 土耳其
#    "KZ",   # 哈萨克斯坦
#    "IN",   # 印度
#    "JP",   # 日本
#    "UK",   # 英国
#    "DE"   # 德国
    ]

# 为每个游戏 ID 创建文件夹并获取多个国家的数据
for game_id in game_ids:
    # 创建以游戏 ID 为名称的文件夹
    if not os.path.exists(game_id):
        os.makedirs(game_id)

    for country in countries:
        # 请求 URL 拼接国家参数
        request_url = f"{url}{country}"
        headers = {
            "Content-Type": "application/json"
        }
        data = [game_id]

        # 发起 POST 请求
        response = requests.post(request_url, headers=headers, data=json.dumps(data))

        # 检查响应状态码
        if response.status_code == 200:
            # 将响应的 JSON 数据保存到文件
            file_path = f"../public/itad/{game_id}/{country}.json"
            with open(file_path, "w", encoding="utf-8") as json_file:
                json.dump(response.json(), json_file, ensure_ascii=False, indent=4)
            print(f"数据已成功保存到 {file_path}")
        else:
            print(f"请求失败，状态码: {response.status_code}, 错误信息: {response.text}")
