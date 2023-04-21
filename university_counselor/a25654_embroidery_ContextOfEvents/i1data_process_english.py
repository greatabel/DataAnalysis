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
with open('data/i0successor_en.csv', 'r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    data_list = []

    # 遍历CSV中的每一行数据
    for row in csv_reader:
        seq_num = row['序号']
        project_num = row['项目编号']
        representative = row['代表性传承人']
        gender = row['性别']
        project_name = row['项目名称']
        category = row['类别']
        announcement = row['公布时间及批次']
        region = row['申报地区或单位']

        # 将CSV中的数据转换为所需的JSON格式，并根据属性计算关联程度
        data_list.append({"word1": f"presenter({representative})", "word2": f"No({seq_num})", "freq": calculate_freq(representative, seq_num)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"ProjectNo({project_num})", "freq": calculate_freq(representative, project_num)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"Sex({gender})", "freq": calculate_freq(representative, gender)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"project_name({project_name})", "freq": calculate_freq(representative, project_name)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"Category({category})", "freq": calculate_freq(representative, category)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"publishdate({announcement})", "freq": calculate_freq(representative, announcement)})
        data_list.append({"word1": f"presenter({representative})", "word2": f"area({region})", "freq": calculate_freq(representative, region)})
        data_list.append({"word1": f"projectname({project_name})", "word2": f"official_date({announcement})", "freq": calculate_freq(project_name, announcement)})
        data_list.append({"word1": f"projectname({project_name})", "word2": f"office_area({region})", "freq": calculate_freq(project_name, region)})

# 保存JSON文件
with open('movie/static/kg_data/2.json', 'w', encoding='utf-8') as jsonfile:
    json.dump(data_list, jsonfile, ensure_ascii=False, indent=2)
