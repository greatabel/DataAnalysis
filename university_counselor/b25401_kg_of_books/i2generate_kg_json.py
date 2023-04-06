import re
import json
import random

# 读取 SQL 文件
with open('data/book.sql', 'r', encoding='utf-8') as f:
    sql = f.read()

# 提取 INSERT 语句
inserts = re.findall(r'INSERT INTO `booktb` VALUES \((.*?)\);', sql)

# 逐个生成 JSON 文件
for insert in inserts:
    # 解析 INSERT 语句的值
    values = insert.split(',')
    id = values[0]
    name = values[1].strip('\'')
    author = values[2].strip('\'')
    type = values[3].strip('\'')
    isbn = values[4].strip('\'')
    foreignability = values[5]
    literatureability = values[6]
    viewability = values[7]
    thinkingability = values[8]
    happyability = values[9]
    score = values[10]
    scorenum = values[11]
    press = values[12].strip('\'')
    label = values[13].strip('\'')
    bookimg = values[14]

    # 构造 JSON 对象
    data = []
    data.append({'word1': name, 'word2': author, 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': press, 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': ' '.join(label.split(',')), 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': type, 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': isbn, 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': score, 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': str(scorenum), 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': 'foreignability', 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': 'literatureability', 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': 'viewability', 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': 'thinkingability', 'freq': round(random.uniform(0, 10), 2)})
    data.append({'word1': name, 'word2': 'happyability', 'freq': round(random.uniform(0, 10), 2)})

    print(data)
    # 生成 JSON 文件
    with open(f'movie/static/kg_data/{id}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)
