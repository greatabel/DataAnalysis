import pandas as pd
import random

# 生成用户画像数据
user_data = pd.DataFrame(columns=["userId", "age", "gender", "city", "longitude", "latitude"])

cities = [
    ("上海", 31.2304, 121.4737),
    ("北京", 39.9042, 116.4074),
    ("广州", 23.1291, 113.2644),
    ("深圳", 22.5431, 114.0579),
    ("天津", 39.3434, 117.3616),
    ("重庆", 29.4316, 106.9123),
    ("苏州", 31.2989, 120.5853),
    ("杭州", 30.2741, 120.1551),
    ("成都", 30.5728, 104.0665),
    ("武汉", 30.5931, 114.3054),
]

for i in range(5000):
    city, latitude, longitude = random.choice(cities)
    user_data = user_data.append({
        "userId": i,
        "age": random.randint(18, 65),
        "gender": random.choice(["Male", "Female"]),
        "city": city,
        "longitude": longitude,
        "latitude": latitude,

    }, ignore_index=True)

user_data.to_csv("../data/user_data.csv", index=False)

# 生成用户行为数据
user_behavior_data = pd.DataFrame(columns=["userId", "itemId", "rating"])
for i in range(5000):
    for j in range(100):
        if random.random() < 0.2:
            user_behavior_data = user_behavior_data.append({
                "userId": i,
                "itemId": j,
                "rating": random.randint(1, 5),
            }, ignore_index=True)

user_behavior_data.to_csv("../data/user_behavior_data.csv", index=False)
