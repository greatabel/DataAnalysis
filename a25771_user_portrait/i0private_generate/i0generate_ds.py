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
    age = random.randint(18, 65)
    gender = random.choice(["Male", "Female"])
    
    if age < 30:
        city, latitude, longitude = random.choice(cities[:2]) if random.random() < 0.8 else random.choice(cities[2:])
    elif gender == "Male":
        city, latitude, longitude = random.choice(cities[2:4]) if random.random() < 0.9 else random.choice(cities[:2] + cities[4:])
    else:
        city, latitude, longitude = random.choice(cities)
    
    user_data = user_data.append({
        "userId": i,
        "age": age,
        "gender": gender,
        "city": city,
        "longitude": longitude,
        "latitude": latitude,
    }, ignore_index=True)

user_data.to_csv("../data/user_data.csv", index=False)

print('#'*20)
# 生成用户行为数据
import pandas as pd
import random

# ... 之前的代码不变 ...

def age_city_related_item(age, city):
    if age < 30:
        if city in ("上海", "北京"):
            return random.randint(0, 49)
        else:
            return random.randint(50, 99)
    elif city in ("广州", "深圳"):
        return random.randint(0, 74)
    else:
        return random.randint(25, 99)

def weighted_rating_by_age(age):
    if age < 30:
        return random.choices([1, 2, 3, 4, 5], weights=[1, 2, 4, 8, 16])[0]
    elif age < 45:
        return random.choices([1, 2, 3, 4, 5], weights=[1, 2, 4, 8, 16])[0]
    else:
        return random.choices([1, 2, 3, 4, 5], weights=[16, 8, 4, 2, 1])[0]

# 生成用户行为数据
user_behavior_data = pd.DataFrame(columns=["userId", "itemId", "rating"])
for i in range(5000):
    user_age = user_data.loc[i, "age"]
    user_city = user_data.loc[i, "city"]
    for j in range(100):
        if random.random() < 0.2:
            user_behavior_data = user_behavior_data.append({
                "userId": i,
                "itemId": age_city_related_item(user_age, user_city),
                "rating": weighted_rating_by_age(user_age),
            }, ignore_index=True)

user_behavior_data.to_csv("../data/user_behavior_data.csv", index=False)
