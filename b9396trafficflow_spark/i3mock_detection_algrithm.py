import random

'''
后续新需求，可以替换这块模拟为真实的yolo算法调用
'''
def mock_process(placeid, img):
    x = 0
    if placeid == "192.168.0.1":
        x = 10
    if placeid == "192.168.0.2":
        x = 15
    if placeid == "192.168.0.3":
        x = 5
    mock_dic = {
        "car_type_small": None,
        "car_type_middle": None,
        "car_type_large": None,
        "car_total_num": None,
    }
    car_type_small = random.randint(0, 20 + x)
    car_type_middle = random.randint(0, 10 + x)
    car_type_large = random.randint(0, 8 + x)
    car_total_num = car_type_small + car_type_middle + car_type_large

    mock_dic["car_type_small"] = car_type_small
    mock_dic["car_type_middle"] = car_type_middle
    mock_dic["car_type_large"] = car_type_large
    mock_dic["car_total_num"] = car_total_num

    return mock_dic
