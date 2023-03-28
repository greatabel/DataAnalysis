import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from termcolor import colored

from i0common import *


# 为提供的 JSON 文件创建变量
folder_path = "v2.0-mini/"
visibility_file = folder_path + "visibility.json"
sensor_file = folder_path + "sensor.json"
scene_file = folder_path + "scene.json"
sample_data_file = folder_path + "sample_data.json"
sample_annotation_file = folder_path + "sample_annotation.json"
sample_file = folder_path + "sample.json"
map_file = folder_path + "map.json"
log_file = folder_path + "log.json"
lidarseg_file = folder_path + "lidarseg.json"
instance_file = folder_path + "instance.json"
ego_pose_file = folder_path + "ego_pose.json"
category_file = folder_path + "category.json"
calibrated_sensor_file = folder_path + "calibrated_sensor.json"

# 加载 JSON 文件
visibility_data = load_json(visibility_file)
sensor_data = load_json(sensor_file)
scene_data = load_json(scene_file)
sample_data = load_json(sample_data_file)
sample_annotation_data = load_json(sample_annotation_file)
sample = load_json(sample_file)
map_data = load_json(map_file)
log_data = load_json(log_file)
lidarseg_data = load_json(lidarseg_file)
instance_data = load_json(instance_file)
ego_pose_data = load_json(ego_pose_file)
category_data = load_json(category_file)
calibrated_sensor_data = load_json(calibrated_sensor_file)



print(
    colored("示例-2:", "blue"), "每个传感器模态的数量。"
)
# 统计每个modality的数量
modality_counts = {}
for item in sensor_data:
    modality = item['modality']
    modality_counts[modality] = modality_counts.get(modality, 0) + 1

# 将结果按照数量从大到小排序
sorted_modality_counts = sorted(modality_counts.items(), key=lambda x: x[1], reverse=True)

# 将结果分为两个列表，一个是modality，一个是数量
modality_names = [item[0] for item in sorted_modality_counts]
modality_values = [item[1] for item in sorted_modality_counts]

# 绘制折线图
plt.plot(modality_names, modality_values, marker='o')
plt.ylabel('Number of Sensors')
plt.title('Sensor Modalities')
plt.show()

# 定义不同类别的关键词
category_keywords = {
    "vehicle.bicycle": ["vehicle.bicycle"],
    "vehicle.car": ["vehicle.car", "vehicle.trailer"],
    "vehicle.bus": ["vehicle.bus.rigid", "vehicle.bus.bendy"],
    "vehicle.truck": ["vehicle.truck"],
    "vehicle.construction": ["vehicle.construction"],
    "vehicle.emergency": ["vehicle.emergency"],
    "vehicle.motorcycle": ["vehicle.motorcycle"],
    "vehicle.other": ["vehicle.other"],
    "human.pedestrian": [
        "human.pedestrian.adult",
        "human.pedestrian.child",
        "human.pedestrian.construction_worker",
        "human.pedestrian.police_officer",
        "human.pedestrian.personal_mobility",
        "human.pedestrian.stroller",
        "human.pedestrian.wheelchair",
    ],
    "movable_object.barrier": ["movable_object.barrier"],
    "movable_object.trafficcone": ["movable_object.trafficcone"],
    "movable_object.pushable_pullable": ["movable_object.pushable_pullable"],
    "movable_object.debris": ["movable_object.debris"],
    "static_object.bicycle_rack": ["static_object.bicycle_rack"],
    "flat.driveable_surface": ["flat.driveable_surface"],
    "flat.sidewalk": ["flat.sidewalk"],
    "flat.terrain": ["flat.terrain"],
    "static.manmade": ["static.manmade"],
    "static.nature": ["static.nature"],
    "static.vegetation": ["static.vegetation"],
    "vehicle.ego": ["vehicle.ego"],
    "": ["unknown"],
}

print(colored("示例-1:", "blue"), "探测到多少种类的目标。")

# 统计每个种类的目标数量
category_counts = {}
for category in category_data:
    category_desc = category["description"]
    for key, values in category_keywords.items():
        if any(value in category_desc for value in values):
            category_counts[key] = category_counts.get(key, 0) + 1
            break

# 绘制柱状图
plt.bar(range(len(category_counts)), list(category_counts.values()), align="center")
plt.xticks(range(len(category_counts)), list(category_counts.keys()), rotation=90)
plt.ylabel("Number of Targets")
plt.title("Target Categories")
plt.show()


# 示例0: 分布图
print(
    colored("示例0:", "blue"), "检查数据集提供的sample的文件格式分布。这个图展示了文件格式（如 jpg 和 npz）在数据集中的分布情况。"
)

sns.set(style="darkgrid")
df1 = pd.DataFrame(sample_data)
plt.figure(figsize=(12, 6))
sns.countplot(data=df1, x="fileformat")
plt.title("File Format Distribution")
plt.show()


# 示例1: 大小分布
print(colored("示例1:", "blue"), "实例大小分布。这个图展示了数据集中不同实例（如车辆、行人等）的尺寸（长x、宽y、高z）分布情况。")

df2 = pd.DataFrame(sample_annotation_data)
sizes = pd.DataFrame(df2["size"].tolist(), columns=["x", "y", "z"])
plt.figure(figsize=(12, 6))
sns.histplot(data=sizes)
plt.title("Instance Size Distribution")
plt.show()

# 示例2: 平移分布
print(colored("示例2:", "blue"), "实例平移分布。这个图展示了数据集中不同实例（如车辆、行人等）在三维空间（x、y、z轴）中的位置分布情况。")

translations = pd.DataFrame(df2["translation"].tolist(), columns=["x", "y", "z"])
plt.figure(figsize=(12, 6))
sns.histplot(data=translations)
plt.title("Instance Translation Distribution")
plt.show()


# 示例3: 旋转分布
print(
    colored("示例3:", "red"),
    "实例旋转分布。简单说就是汉密尔顿4元数度量旋转角。度量数据集中物体的旋转情。 \
	这个图展示了数据集中不同实例（如车辆、行人等）在三维空间中的旋转（四元数表示：x、y、z、w）分布情况。",
)
rotations = pd.DataFrame(df2["rotation"].tolist(), columns=["x", "y", "z", "w"])
plt.figure(figsize=(12, 6))
sns.histplot(data=rotations)
plt.title("Instance Rotation Distribution")
plt.show()


# 势力4: 统计饼图
print(colored("示例4:", "red"), "实前10个出现次数最多的sensor_token分布情况。")
calibrated_sensor_df = pd.DataFrame(calibrated_sensor_data)

# 统计每个sensor_token出现的次数
counts = calibrated_sensor_df["sensor_token"].value_counts()

# 选取前10个出现次数最多的sensor_token
top_10 = counts.nlargest(10)

# 生成饼图
plt.figure(figsize=(8, 8))
plt.pie(top_10.values, labels=top_10.index, autopct="%1.1f%%")
plt.title("Top 10 Most Common Sensor Tokens")
plt.show()



