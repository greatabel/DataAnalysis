from nuscenes.nuscenes import NuScenes
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import BSpline, make_interp_spline

from scipy.interpolate import splprep, splev

def plot_sensor_fov(nusc: NuScenes, my_sample, sensor, color, label):
    # 获取当前传感器数据
    sensor_data = nusc.get('sample_data', my_sample['data'][sensor])
    
    # 获取传感器的校准数据
    sensor_calib = nusc.get('calibrated_sensor', sensor_data['calibrated_sensor_token'])
    
    # 使用传感器校准数据中的旋转和转换数据
    rotation = Quaternion(sensor_calib['rotation'])
    x, y, z = sensor_calib['translation']

    # 保持其他代码不变，并使用以上的x, y和rotation替换原本硬编码的值
    
nusc = NuScenes(version='v1.0-mini', dataroot='/data/sets/nuscenes', verbose=True)

my_scene = nusc.scene[0]
my_sample = nusc.get('sample', my_scene['first_sample_token'])

plt.figure(figsize=(10, 10))

# Front camera
plot_sensor_fov(nusc, my_sample, 'CAM_FRONT', 'red', 'Front Camera')




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




