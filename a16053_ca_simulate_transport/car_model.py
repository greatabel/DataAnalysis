import random


def init_car_model(
    road_2d_matrix, leng, cell2, way, tesla_rate, car_p, fast_through_area_ratio
):
    tesla_rate = tesla_rate * (1 + fast_through_area_ratio)
    # 0 代表这个位置是空的，暂时还没有车🚗占据
    if road_2d_matrix[way][0] == 0:
        leng[way] = leng[way] + 1
        if random.randint(1, 100) <= car_p * (1 - tesla_rate) * 100:
            # 燃油车
            road_2d_matrix[way][0] = 1
        elif random.randint(1, 100) <= car_p * tesla_rate * 100:
            # 电动汽车
            road_2d_matrix[way][0] = 2
    cell2[way][0] = random.randint(0, 2)
