import random


def init_car_model(cell_temp, leng, cell2, way, tesla_rate, car_p):
    # 0 代表这个位置是空的，暂时还没有车🚗占据
    if cell_temp[way][0] == 0:
        leng[way] = leng[way] + 1
        if random.randint(1, 100) <= car_p * (1 - tesla_rate) * 100:
            # 燃油车
            cell_temp[way][0] = 1
        elif random.randint(1, 100) <= car_p * tesla_rate * 100:
            # 电动汽车
            cell_temp[way][0] = 2
    cell2[way][0] = random.randint(0, 2)
