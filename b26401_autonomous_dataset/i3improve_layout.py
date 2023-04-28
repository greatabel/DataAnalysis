'''
calibrated_sensor.json文件与sample_data.json文件最相关。
sample_data.json文件包含了与传感器记录的数据样本相关的信息。
它们之间的关系是通过calibrated_sensor.json中的sensor_token与sample_data.json中的calibrated_sensor_token进行匹配

传感器覆盖分析：分析不同传感器的场景覆盖和重叠区域，以评估传感器布局的有效性和冗余性。
这可以通过结合calibrated_sensor.json中的传感器校准信息和sample_data.json中的数据样本进行实现。
传感器覆盖分析有助于优化传感器布局，提高场景感知的可靠性和鲁棒性
'''
# import json
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.patches import Polygon
# from scipy.spatial.transform import Rotation as R

# # Load calibrated_sensor.json and sample_data.json
# with open('v2.0-mini/calibrated_sensor1.json', 'r') as f:
#     calibrated_sensors = json.load(f)
# with open('v2.0-mini/sample_data1.json', 'r') as f:
#     sample_data = json.load(f)

# # Filter camera sensor data
# camera_calibrated_sensors = [sensor for sensor in calibrated_sensors if 'camera_intrinsic' in sensor]
# camera_sample_data = [data for data in sample_data if data['fileformat'] == 'jpg']


# def compute_fov_polygon(calibrated_sensor, sample_data, max_distance=50):
#     # Get intrinsic and extrinsic camera parameters
#     K = np.array(calibrated_sensor['camera_intrinsic'])
#     rotation = R.from_quat(calibrated_sensor['rotation'])
#     translation = np.array(calibrated_sensor['translation'])

#     # Define image corners in pixel coordinates
#     img_corners = np.array([
#         [0, 0, 1],
#         [0, sample_data['height'] - 1, 1],
#         [sample_data['width'] - 1, sample_data['height'] - 1, 1],
#         [sample_data['width'] - 1, 0, 1]
#     ]).T

#     # Compute image corners in world coordinates
#     world_corners = rotation.as_matrix().T @ np.linalg.inv(K) @ img_corners
#     world_corners = world_corners * translation[2] / world_corners[2, :]
#     world_corners[:2, :] += np.array(translation[:2]).reshape(-1, 1)

#     # Compute direction vectors for image corners
#     direction_vectors = world_corners[:2, :] - np.array(translation[:2]).reshape(-1, 1)
#     direction_vectors /= np.linalg.norm(direction_vectors, axis=0)

#     # Compute far plane corners in world coordinates
#     far_plane_corners = np.array(translation[:2]).reshape(-1, 1) + max_distance * direction_vectors

#     # Combine near and far plane corners to create FOV polygon
#     fov_polygon = np.hstack([world_corners[:2, :], far_plane_corners])

#     return fov_polygon





# # Compute FOV polygons for each camera sensor
# fov_polygons = []
# for sensor in camera_calibrated_sensors:
#     for data in camera_sample_data:
#         if sensor['token'] == data['calibrated_sensor_token']:
#             fov_polygons.append(compute_fov_polygon(sensor, data))

# # Plot FOV polygons
# # Generate a color map with unique colors for each sensor
# num_sensors = len(camera_calibrated_sensors)
# colors = plt.cm.get_cmap('tab10', num_sensors)

# # Plot FOV polygons with unique colors
# fig, ax = plt.subplots()
# for i, (sensor, polygon) in enumerate(zip(camera_calibrated_sensors, fov_polygons)):
#     ax.add_patch(Polygon(polygon.T, edgecolor=colors(i), alpha=0.3, fill=False, label=f'Sensor {i + 1}'))

# ax.set_aspect('equal', 'box')
# plt.xlabel('X (m)')
# plt.ylabel('Y (m)')
# plt.title('Camera Sensors FOV Coverage')
# plt.legend()
# plt.grid()
# plt.show()

# 版本2
# import matplotlib.pyplot as plt
# import numpy as np

# def plot_sensor_fov(x, y, rotation, color, label):
#     width = 60
#     height = 40
#     corners = np.array([[-width/2, -height/2, 1], [width/2, -height/2, 1], [width/2, height/2, 1], [-width/2, height/2, 1]])
#     rot_matrix = np.array([[np.cos(rotation), -np.sin(rotation)], [np.sin(rotation), np.cos(rotation)]])
#     transformed_corners = np.dot(rot_matrix, corners[:, :2].T).T
#     transformed_corners += np.array([x, y])
#     plt.fill(transformed_corners[:, 0], transformed_corners[:, 1], color, alpha=0.5, label=label)

# plt.figure(figsize=(10, 10))

# # Front camera
# plot_sensor_fov(4, 0, np.radians(0), 'red', 'Front Camera')

# # Rear camera
# plot_sensor_fov(-4, 0, np.radians(180), 'blue', 'Rear Camera')

# # Front-left and front-right cameras
# plot_sensor_fov(2, 2, np.radians(-30), 'green', 'Front-left Camera')
# plot_sensor_fov(2, -2, np.radians(30), 'purple', 'Front-right Camera')

# # Rear-left and rear-right cameras
# plot_sensor_fov(-2, 2, np.radians(210), 'orange', 'Rear-left Camera')
# plot_sensor_fov(-2, -2, np.radians(-210), 'cyan', 'Rear-right Camera')

# # Lidar sensor
# plot_sensor_fov(0, 0, np.radians(0), 'brown', 'Lidar Sensor')

# # Vehicle shape
# vehicle = plt.Rectangle((-4, -2), 8, 4, fill=False, edgecolor='black', linewidth=1.5)
# plt.gca().add_patch(vehicle)

# plt.xlim(-20, 20)
# plt.ylim(-20, 20)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Sensor FOV Coverage')
# plt.grid(True)
# plt.gca().set_aspect('equal', adjustable='box')
# plt.legend(loc='upper right')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

from scipy.interpolate import splprep, splev

def plot_sensor_fov(x, y, rotation, color, label):
    width = 60
    height = 40
    n_points = 10
    np.random.seed(42)
    randomness = np.random.normal(0, 1, (n_points, 2))
    
    corners = np.array([np.linspace(-width/2, width/2, n_points), -height/2 * np.ones(n_points)]).T + randomness
    corners = np.vstack((corners, np.array([np.linspace(width/2, width/2, n_points), np.linspace(-height/2, height/2, n_points)]).T + randomness))
    corners = np.vstack((corners, np.array([np.linspace(width/2, -width/2, n_points), height/2 * np.ones(n_points)]).T + randomness))
    corners = np.vstack((corners, np.array([np.linspace(-width/2, -width/2, n_points), np.linspace(height/2, -height/2, n_points)]).T + randomness))
    
    rot_matrix = np.array([[np.cos(rotation), -np.sin(rotation)], [np.sin(rotation), np.cos(rotation)]])
    transformed_corners = np.dot(rot_matrix, corners.T).T
    transformed_corners += np.array([x, y])

    tck, u = splprep(transformed_corners.T, s=0, per=True)
    new_u = np.linspace(0, 1, len(transformed_corners) * 10)
    new_points = np.array(splev(new_u, tck)).T

    plt.fill(new_points[:, 0], new_points[:, 1], color, alpha=0.5, label=label)


plt.figure(figsize=(10, 10))

# Front camera
plot_sensor_fov(4, 0, np.radians(0), 'red', 'Front Camera')

# Rear camera
plot_sensor_fov(-4, 0, np.radians(180), 'blue', 'Rear Camera')

# Front-left and front-right cameras
plot_sensor_fov(4, 4, np.radians(-40), 'green', 'Front-left Camera')
plot_sensor_fov(4, -4, np.radians(40), 'purple', 'Front-right Camera')

# Rear-left and rear-right cameras
plot_sensor_fov(-4, 4, np.radians(210), 'orange', 'Rear-left Camera')
plot_sensor_fov(-4, -4, np.radians(-210), 'cyan', 'Rear-right Camera')

# Lidar sensor
plot_sensor_fov(0, 0, np.radians(0), 'brown', 'Lidar Sensor')

# Vehicle shape
vehicle = plt.Rectangle((-4, -2), 8, 4, fill=False, edgecolor='black', linewidth=1.5)
plt.gca().add_patch(vehicle)

plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Sensor FOV Coverage')
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend(loc='upper right')
plt.show()



