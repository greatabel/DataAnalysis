import os
import jieba
import spacy
import csv
import json
import random


def preprocess_text(text):
    words = jieba.cut(text)
    clean_text = " ".join(words)
    return clean_text

def extract_triplets(text):
#     三元组的结构是（实体1，关系，实体2）。

# 'nsubj'表示名词主语（nominal subject），意味着实体1是实体2的主语。例如，在三元组 ('教程', 'nsubj', '视觉') 中，'教程'是'视觉'的主语。

# 'dobj'表示直接宾语（direct object），意味着实体1是实体2的宾语。例如，在三元组 ('教程', 'dobj', '检测') 中，'教程'是'检测'的宾语
    nlp = spacy.load("zh_core_web_sm")
    doc = nlp(text)

    triplets = []
    for token in doc:
        if token.dep_ in ("nsubj", "dobj"):
            subject = token.head.text
            relation = token.dep_
            obj = token.text
            triplet = (subject, relation, obj)
            triplets.append(triplet)
    return triplets

def save_triplets_to_csv(triplets, output_file):
    with open(output_file, "w", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["word1", "word2", "freq"])
        for triplet in triplets:
            writer.writerow([triplet[0], f"{triplet[1]} {triplet[2]}", 1])

def calculate_freq(attr1, attr2):
    set1 = set(attr1.split())
    set2 = set(attr2.split())

    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    # print(set1, set2, intersection, union)

    if intersection == 0:
        intersection = random.randint(1, union)
    r = intersection / union
    r = r * 10
    return r

def generate_json(triplets, output_file):
    data = [
        {"word1": triplet[0], "word2": f"{triplet[2]}", "freq": calculate_freq(triplet[0], triplet[2])}
        for triplet in triplets
        if len(triplet[0]) > 1 and len(triplet[2]) > 1
    ]

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    data_dir = "data"

    all_triplets = []

    for file in os.listdir(data_dir)[0:5]:
        if file.endswith(".txt"):
            print('preprocess_text=>', file)
            with open(os.path.join(data_dir, file), "r", encoding="utf-8") as f:
                content = f.read()

                clean_text = preprocess_text(content)

                triplets = extract_triplets(clean_text)
                print('triplets=', triplets)
                all_triplets.extend(triplets)

    selected_triplets = all_triplets[:2023]

    # 保存三元组到CSV文件
    save_triplets_to_csv(selected_triplets, "triplets.csv")

    # 生成JSON文件
    generate_json(selected_triplets[:50], "movie/static/kg_data/default.json")


