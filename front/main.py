# from os.path import dirname, abspath
# import sys

# parent_dir = dirname(dirname(abspath(__file__)))  # 追加
# print(parent_dir)  # 追加
# if parent_dir not in sys.path:  # 追加
#     sys.path.append(parent_dir)  # 追加

# from backend.main import CreateItemDto
import json
import requests

API_URL = "http://localhost:8000/items/"


# 1. リクエストをpostで送る
# 2. リクエストのbodyにItemDtoの値を入れる
# 3. レスポンスを受け取る
# 4. レスポンスのbodyを表示する
def create_item():
    body = {
        "shopInfo": {
            "name": "shop1",
            "location": "tokyo",
        },
        "items": [
            {"name": "item1", "price": 100},
            {"name": "item2", "price": 200},
        ],
    }
    res = requests.post(API_URL, json.dumps(body))
    print(res.status_code)
    return res.json()


# 実行
if __name__ == "__main__":
    data = create_item()
    print(data)
