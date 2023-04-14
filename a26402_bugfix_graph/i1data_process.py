import csv
import json
import random

# 刺绣图谱数据处理

def calculate_freq(attr1, attr2):
    set1 = set(attr1.split())
    set2 = set(attr2.split())

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    print(set1, set2, intersection, union)

    if intersection == 0:
        intersection = random.randint(1, union)
    r = intersection / union
    r = r * 10
    return r

# 读取CSV文件内容
with open('data/bug_solution.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data_list = []

    # 遍历CSV中的每一行数据
    for row in csv_reader:
        bug = row['bug']
        solution = row['solution']


        # 将CSV中的数据转换为所需的JSON格式，并根据属性计算关联程度
        data_list.append({"word1": f"Q({bug})", "word2": f"A({solution})", "freq": calculate_freq(bug, solution)})

# 保存JSON文件
with open('movie/static/kg_data/3.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data_list, jsonfile, ensure_ascii=False, indent=2)
