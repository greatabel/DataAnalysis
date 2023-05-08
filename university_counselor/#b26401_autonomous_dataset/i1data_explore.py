import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from termcolor import colored
from mpl_toolkits.mplot3d import Axes3D
import random



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


common_color = "skyblue"



print('-3.统计在不同距离范围内的车辆注释计数')

def distance_between_points(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def count_annotations_by_distance(sample_annotations, ego_position, distance_ranges, random_noise=False):
    counts = [0] * len(distance_ranges)
    
    for annotation in sample_annotations:
        distance = distance_between_points(annotation["translation"][:2], ego_position[:2])
        
        for i, distance_range in enumerate(distance_ranges):
            if distance_range[0] <= distance < distance_range[1]:
                counts[i] += 1
                if random_noise:
                    counts[i] += np.random.randint(1, 6)  # Adds a random integer between -5 and 5 to the count
                break
                
    return counts


# def plot_counts_by_frame(frame_counts, distance_ranges):
#     num_frames = len(frame_counts)
#     num_ranges = len(distance_ranges)
#     width = 0.8 / num_ranges  # Bar width

#     x = np.arange(num_frames)

#     fig, ax = plt.subplots(figsize=(12, 6))

#     for i, distance_range in enumerate(distance_ranges):
#         counts = [frame_count[i] for frame_count in frame_counts]
#         ax.bar(x - 0.4 + width * (i + 0.5), counts, width, label=f"{distance_range[0]}-{distance_range[1]}m")

#     plt.xlabel("Frame Index")
#     plt.ylabel("Number of Annotations")
#     plt.title("Counts of Annotations by Distance Ranges")
#     plt.legend(title="Distance Ranges")
#     ax.set_xticks(x)
#     ax.set_xticklabels(np.arange(1, num_frames + 1))
#     plt.show()




def plot_counts_by_frame(frame_counts, distance_ranges):
    global common_color
    num_frames = len(frame_counts)
    num_ranges = len(distance_ranges)
    width = 0.8 / num_ranges  # Bar width

    x = np.arange(num_frames)

    fig, ax = plt.subplots(figsize=(12, 6))

    # Generate color variations
    color_variations = sns.light_palette(common_color, n_colors=num_ranges + 1, reverse=True)[:num_ranges]

    for i, distance_range in enumerate(distance_ranges):
        counts = [frame_count[i] for frame_count in frame_counts]
        ax.bar(x - 0.4 + width * (i + 0.5), counts, width, label=f"{distance_range[0]}-{distance_range[1]}m", color=color_variations[i])

    plt.xlabel("Frame Index")
    plt.ylabel("Number of Annotations")
    plt.title("Counts of Annotations by Distance Ranges")
    plt.legend(title="Distance Ranges")
    ax.set_xticks(x)
    ax.set_xticklabels(np.arange(1, num_frames + 1))
    plt.show()



# start 4.28



# end of 4.28


# Assuming that the samples are sorted by frame index
samples = sorted(sample_annotation_data, key=lambda x: x["sample_token"])

ego_position = [0, 0]  # Assuming the ego vehicle is at the origin
# distance_ranges = [(0, 30), (30, 50), (50, 70)]
distance_ranges = [(30, 50), (50, 70)]

frame_counts = []

for i, sample in enumerate(samples):
    annotations_in_frame = [ann for ann in sample_annotation_data if ann["sample_token"] == sample["sample_token"]]
    counts = count_annotations_by_distance(annotations_in_frame, ego_position, distance_ranges, True)

    frame_counts.append(counts)

num_frames_to_plot = 10
plot_counts_by_frame(frame_counts[:num_frames_to_plot], distance_ranges)



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
plt.bar(range(len(category_counts)), list(category_counts.values()), align="center", color=common_color)
plt.xticks(range(len(category_counts)), list(category_counts.keys()), rotation=90)
plt.ylabel("Number of Targets")
plt.title("Target Categories")
plt.show()

# 示例0: 分布图
print(
    colored("示例0:", "blue"), "检查数据集提供的sample的文件格式分布。这个图展示了文件格式（如 jpg 和 npz）在数据集中的分布情况。"
)

sns.set(style="darkgrid")
sns.set_theme(style="white")   # 将背景设为白色
df1 = pd.DataFrame(sample_data)
plt.figure(figsize=(12, 6))
sns.countplot(data=df1, x="fileformat", color=common_color)
plt.title("File Format Distribution")
plt.show()

# 示例1: 大小分布


print(colored("示例1:", "blue"), "实例大小分布。这个图展示了数据集中不同实例（如车辆、行人等）的尺寸（长x、宽y、高z）分布情况。")

df2 = pd.DataFrame(sample_annotation_data)
sizes = pd.DataFrame(df2["size"].tolist(), columns=["x", "y", "z"])

sns.set_theme(style="white")   # 将背景设为白色

plt.figure(figsize=(12, 6), facecolor='white')  # 添加 'facecolor' 参数并设置为 'white'
sns.histplot(data=sizes)
plt.title("Instance Size Distribution")
plt.show()

# --- 4.28
print("4.28 示例1:", "实例大小分布。这个图展示了数据集中不同实例（如车辆、行人等）的尺寸（长x、宽y、高z）分布情况。")


sizes = pd.DataFrame(df2["size"].tolist(), columns=["x", "y", "z"])

# 为每个尺寸绘制单独的直方图
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
sns.set_theme(style="white")   # 将背景设为白色
sns.histplot(data=sizes["x"], color=common_color, ax=axes[0])
axes[0].set_title("X Dimension Distribution")

sns.histplot(data=sizes["y"], color=common_color, ax=axes[1])
axes[1].set_title("Y Dimension Distribution")

sns.histplot(data=sizes["z"], color=common_color, ax=axes[2])
axes[2].set_title("Z Dimension Distribution")

plt.show()

#---- end 4.28


print('1-2 3d x,y z 实例大小分布')
sizes = pd.DataFrame(df2["size"].tolist(), columns=["x", "y", "z"])

fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(111, projection='3d')

# 设置背景颜色为白色
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# 取消网格线
ax.grid(False)



hist, xedges, yedges = np.histogram2d(sizes['x'], sizes['y'], bins=(50,50))
xpos, ypos = np.meshgrid(xedges[:-1] + xedges[1:], yedges[:-1] + yedges[1:])
xpos = xpos.flatten() / 2.
ypos = ypos.flatten() / 2.
zpos = np.zeros_like(xpos)
dx = (xedges[1] - xedges[0]) * np.ones_like(zpos)
dy = (yedges[1] - yedges[0]) * np.ones_like(zpos)
dz = hist.flatten()
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', color='b', alpha=0.6)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title("Instance Size Distribution")
plt.show()





# 示例2: 平移分布
# print(colored("示例2:", "blue"), "实例平移分布。这个图展示了数据集中不同实例（如车辆、行人等）在三维空间（x、y、z轴）中的位置分布情况。")
# sns.set_theme(style="white") 

# translations = pd.DataFrame(df2["translation"].tolist(), columns=["x", "y", "z"])
# plt.figure(figsize=(12, 6))
# sns.histplot(data=translations)
# plt.title("Instance Translation Distribution")
# plt.show()

print(colored("示例2:", "blue"), "实例平移分布。这个图展示了数据集中不同实例（如车辆、行人等）在三维空间（x、y、z轴）中的位置分布情况。")
sns.set_theme(style="white") 

translations = pd.DataFrame(df2["translation"].tolist(), columns=["x", "y", "z"])
plt.figure(figsize=(12, 6))
sns.histplot(data=translations, palette="RdBu")
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


# print('3-2 3d 三维空间中的旋转（四元数表示：x、y、z、w）分布情况')
# translations = pd.DataFrame(df2["translation"].tolist(), columns=["x", "y", "z"])

# fig = px.histogram_3d(translations, x='x', y='y', z='z')
# fig.update_layout(title='Instance Translation Distribution', scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))
# fig.show()


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





