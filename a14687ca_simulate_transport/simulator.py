import numpy as np
import random
import copy
import time


import matplotlib.pyplot as plt
from termcolor import colored, cprint

from car_model import init_car_model
from visualization import visulize_to_png, show_img, show_simplify_to_path

fast_through_area_ratio = 1 / 6


def custom_map_2d_to_1d(x, width):
    speedup = 1
    change_lane_rate = 1
    cular_scale = 1
    if 0 < x < width * 1 / 3:
        speedup = 1
        change_lane_rate = 1
        cular_scale = 1
    elif width / 3 < x <= width / 3 + fast_through_area_ratio:
        speedup = 2
        change_lane_rate = 1.5
        cular_scale = 2
    else:
        speedup = 1
        change_lane_rate = 2
        cular_scale = 1
    return speedup, change_lane_rate, cular_scale


def car_simulate_driving(way, width):
    for j in range(0, width - 1):

        # 获得当前位置街区的加速因子，换道印子，元胞扩大比例
        speedup, change_lane_rate, cular_scale = custom_map_2d_to_1d(j, width)

        if j == 0 and cell[way][0] != 0:
            x = 0
            for i in range(j + 1, j + 4):
                if cell[way][i] != 0:
                    x = 1
            if x == 0:
                road_2d_matrix[way][1] = road_2d_matrix[way][0]
                road_2d_matrix[way][0] = 0
                cell2[way][1] = cell2[way][0]
                cell2[way][0] = -1
        elif cell[way][j] != 0:
            if cell2[way][j] == way:
                cell2[way][j] = -1
            if cell2[way][j] != -1 and road_2d_matrix[way][j] == 1:
                a = change_way(way, j)
                if a == 0:
                    continue
            elif cell2[way][j] != -1 and road_2d_matrix[way][j] == 2 and j + 5 + way > width:
                a = change_way(way, j)
                if a == 0:
                    continue
            x = 0
            for i in range(j + 1, min(j + 3, width - 1)):
                if cell[way][i] != 0:
                    x = 1
            if x == 0:
                if (
                    j * cular_scale + 3 < width - 4
                    and cell[way][j + 3] == 0
                    and road_2d_matrix[way][j] == 1
                    and random.randint(1, 100) <= 20
                ):
                    road_2d_matrix[way][j + 2] = road_2d_matrix[way][j]
                    road_2d_matrix[way][j] = 0
                    cell2[way][j + 2] = cell2[way][j]
                    cell2[way][j] = 0
                    k = j + 2 * speedup
                else:
                    road_2d_matrix[way][j + 1] = road_2d_matrix[way][j]
                    road_2d_matrix[way][j] = 0
                    cell2[way][j + 1] = cell2[way][j]
                    cell2[way][j] = 0
                    k = min(j + 1, width - 2)
                if road_2d_matrix[way][k] == 1:
                    if random.randint(1, 100) <= 5 and road_2d_matrix[way][k - 1] == 0:
                        road_2d_matrix[way][k - 1] = 1
                        road_2d_matrix[way][k] = 0
                        cell2[way][k - 1] = cell2[way][k]
                        cell2[way][k] = -1
                    elif random.randint(1, 100) <= 5 and road_2d_matrix[way][k + 1] == 0:
                        road_2d_matrix[way][k + 1] = 1
                        road_2d_matrix[way][k] = 0
                        cell2[way][k + 1] = cell2[way][k]
                        cell2[way][k] = -1


def off_road(way):
    if road_2d_matrix[way][width - 1] != 0 and cell2[way][width - 1] == -1:
        leng[3] = leng[3] + 1
        leng[way] = leng[way] - 1
        road_2d_matrix[way][width - 1] = 0


def change_way(way, local):
    m = 0
    n = 0
    if way == 1:
        if cell2[way][local] != way:
            for i in range(local - 3, min(local + 4, width - 1)):
                if cell[cell2[way][local]][i] != 0:
                    m = 1
            if m == 0:
                road_2d_matrix[cell2[way][local]][local + 1] = road_2d_matrix[way][local]
                road_2d_matrix[way][local] = 0
                leng[way] = leng[way] - 1
                leng[cell2[way][local]] = leng[cell2[way][local]] + 1
                cell2[cell2[way][local]][local + 1] = -1
                cell2[cell2[way][local]][local] = 0
        if m == 0:
            return 0
        else:
            return 1
    if way == 0:
        if cell2[way][local] != way:
            for i in range(local - 3, min(local + 4, width - 1)):
                if cell[1][i] != 0:
                    m = 1
            if m == 0:
                road_2d_matrix[1][local + 1] = road_2d_matrix[way][local]
                road_2d_matrix[way][local] = 0
                leng[way] = leng[way] - 1
                leng[1] = leng[1] + 1
                cell2[1][local + 1] = cell2[way][local]
                cell2[way][local] = 0
        if m == 0:
            return 0
        else:
            return 1
    if way == 2:
        if cell2[way][local] != way:
            for i in range(local - 3, min(local + 4, width - 1)):
                if cell[1][i] != 0:
                    m = 1
            if m == 0:
                road_2d_matrix[1][local + 1] = road_2d_matrix[way][local]
                road_2d_matrix[way][local] = 0
                leng[way] = leng[way] - 1
                leng[1] = leng[1] + 1
                cell2[1][local + 1] = cell2[way][local]
                cell2[way][local] = 0
        if m == 0:
            return 0
        else:
            return 1


if __name__ == "__main__":
    show_img("resources/i1geographical_urban.jpg")

    time.sleep(1)

    show_simplify_to_path()

    length = 3
    width = 30

    d = 0
    cell = np.zeros((length, width), int)
    road_2d_matrix = copy.deepcopy(cell)
    cell2 = copy.deepcopy(cell)
    for i in range(0, length):
        for j in range(0, width):
            road_2d_matrix[i][j] = 0
    for i in range(0, length):
        for j in range(0, width):
            cell2[i][j] = -1

    global leng
    leng = {0: 0, 1: 0, 2: 0, 3: 0}
    list1 = []
    # for i in range(0, 100):
    for i in range(0, 5):
        welcome = colored(
            "#" * 10 + " This turn of car_simulate_driving: " + str(i) + "#" * 10,
            "red",
            attrs=["reverse", "blink"],
        )
        print(welcome, "\n")
        # print("i", "=" * 10, i)
        while True:
            if d % 4 == 0:
                init_car_model(
                    road_2d_matrix, leng, cell2, 0, i / 5, 0.3, fast_through_area_ratio
                )
                # init_car_model(road_2d_matrix, leng, cell2,  0, i/100, 0.3)
            if d % 3 == 0:
                init_car_model(
                    road_2d_matrix, leng, cell2, 1, i / 5, 0.3, fast_through_area_ratio
                )
            if d % 5 == 0:
                init_car_model(
                    road_2d_matrix, leng, cell2, 2, i / 5, 0.3, fast_through_area_ratio
                )
            cell = copy.deepcopy(road_2d_matrix)
            # 显示每一轮的图像
            # plt.imshow(cell, aspect='auto')
            plt.imshow(cell)
            plt.pause(0.0000000001)
            car_simulate_driving(0, width)
            car_simulate_driving(1, width)
            car_simulate_driving(2, width)
            off_road(0)
            off_road(1)
            off_road(2)
            d = d + 1
            # if leng[3] >= 2000:
            if leng[3] >= 10:
                list1.append(d)
                d = 0
                leng[3] = 0
                break
            print("turn:", len(list1))
            time.sleep(random.uniform(0.1, 0.3))
            print("car number off_road:", leng[3])
            msg = colored(
                "#" * 10
                + " The accumulate car_simulate_driving lan: "
                + str(d)
                + " "
                + "#" * 10,
                "blue",
                attrs=["reverse", "blink"],
            )
            print(msg, "\n")

    print(list1)

    # plt.show(block=False)
    # plt.pause(0.2)

    x = np.arange(0, 1, 0.2)
    print("x=", x)
    # x = np.arange(0, 1, 0.01)
    y = list1
    visulize_to_png(x, y)
