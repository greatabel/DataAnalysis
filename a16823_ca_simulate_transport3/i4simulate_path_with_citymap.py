
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from termcolor import colored, cprint

import random
import time
import statistics
from matplotlib import pyplot
import seaborn as sns

from mygrid import Grid
from my_unittype import unit_types, inners, parkings, heats
from car_district_setting import CarSetting
from visualization import visulize_to_png, show_img, show_simplify_to_path
import i2simulator 


ALL_PATHS = []


def mycar_walking(start, end, generated_map=[]):
    # 待访问的格子
    open_list = []
    # 已访问的格子
    close_list = []
    # 把起点加入open_list
    open_list.append(start)
    # 主循环，每一轮检查一个当前方格节点
    while len(open_list) > 0:
        # 在open_list中查找 F值最小的节点作为当前方格节点
        current_grid = find_current_grid(open_list)
        # 当前方格节点从openList中移除
        open_list.remove(current_grid)
        # 当前方格节点进入 closeList
        close_list.append(current_grid)
        # 找到所有邻近节点
        neighbors = find_neighbors(current_grid, open_list, close_list, generated_map)
        for grid in neighbors:
            if grid not in open_list:
                # 邻近节点不在openList中，标记父亲、G、H、F，并放入openList
                grid.init_grid(current_grid, end)
                open_list.append(grid)
        # 如果终点在openList中，直接返回终点格子
        for grid in open_list:
            if (grid.x == end.x) and (grid.y == end.y):
                return grid
    # openList用尽，仍然找不到终点，说明终点不可到达，返回空
    return None


def find_current_grid(open_list=[]):
    temp_grid = open_list[0]
    for grid in open_list:
        if grid.f < temp_grid.f:
            temp_grid = grid
    return temp_grid


def find_neighbors(grid, open_list=[], close_list=[], generated_map=[]):
    grid_list = []
    if is_valid_grid(grid.x, grid.y - 1, open_list, close_list, generated_map):
        grid_list.append(Grid(grid.x, grid.y - 1))
    if is_valid_grid(grid.x, grid.y + 1, open_list, close_list, generated_map):
        grid_list.append(Grid(grid.x, grid.y + 1))
    if is_valid_grid(grid.x - 1, grid.y, open_list, close_list, generated_map):
        grid_list.append(Grid(grid.x - 1, grid.y))
    if is_valid_grid(grid.x + 1, grid.y, open_list, close_list, generated_map):
        grid_list.append(Grid(grid.x + 1, grid.y))
    return grid_list


def is_valid_grid(x, y, open_list=[], close_list=[], generated_map=[]):
    MAZE = generated_map
    # 是否超过边界
    if x < 0 or x >= len(MAZE) or y < 0 or y >= len(MAZE[0]):
        return False
    # 是否有障碍物
    if MAZE[x][y] == 1:
        return False
    # 是否已经在open_list中
    if contain_grid(open_list, x, y):
        return False
    # 是否已经在closeList中
    if contain_grid(close_list, x, y):
        return False
    return True


def contain_grid(grids, x, y):
    for grid in grids:
        if (grid.x == x) and (grid.y == y):
            return True
    return False


def all_walkable(generated_map):
    walkables = []
    for i in range(0, len(generated_map)):
        for j in range(0, len(generated_map[0])):
            if generated_map[i][j] != 1 :
                walkables.append([i, j, generated_map[i][j]])
    return walkables



def single_turn(unittype, generated_map, CarSetting):
    walkables = all_walkable(generated_map)
    # print('walkables=', walkables, '#-# '*10)

    #设置随机数种子seed
    np.random.seed(456789)
    #生成5个均值为len(walkables)//20，标准差为5的正态分布样本,模拟电量
    r = np.random.normal(loc=len(walkables)//20, scale=5, size=5)

    simulate_battery_init = int(r[random.randint(0, 4)])
    print('正态分布样 simulate_battery_init:', simulate_battery_init)
    s, e = None, None
    #模拟早上和晚上
    if random.randint(0, 1) == 0:
        # 模拟早上
        s = walkables[random.randint(0, len(walkables)-1)]
        while s[2] != 2:
            s = walkables[random.randint(0, len(walkables)-1)]
        e = walkables[random.randint(0, len(walkables)-1)]
    else:
        # 模拟晚上,正好相反
        e = walkables[random.randint(0, len(walkables)-1)]
        while e[2] != 2:
            e = walkables[random.randint(0, len(walkables)-1)]
        s = walkables[random.randint(0, len(walkables)-1)]
    # 更多场景 可以修改上面的代码

    start_grid = Grid(s[0], s[1])
    end_grid = Grid(e[0], e[1]) 

    print('-'*10, 'run new simulation turn', '-'*10, '\n')
    # 设置起点和终点
    # start_grid = Grid(2, 1)
    # end_grid = Grid(2, 5)
    # if CarSetting.behavior_type == 0 :
    #     s = walkables[random.randint(0, len(walkables)//2)]
    #     e = walkables[random.randint(len(walkables)//2, len(walkables)-1)]
    #     start_grid = Grid(s[0], s[1])
    #     end_grid = Grid(e[0], e[1])   
    # if CarSetting.behavior_type == 1:
    #     s = walkables[random.randint(0, len(walkables)//2)]
    #     e = walkables[random.randint(len(walkables)//2, len(walkables)-1)]
    #     start_grid = Grid(s[0], s[1])
    #     if random.randint(0, 4) > 2:
    #         end_grid = Grid(parkings[unittype][0], parkings[unittype][1])
    #     else:
    #         end_grid = Grid(e[0], e[1]) 
    # if CarSetting.behavior_type == 2:
    #     s = walkables[random.randint(0, len(walkables)//2)]
    #     e = walkables[random.randint(len(walkables)//2, len(walkables)-1)]
    #     if random.randint(0, 4) > 2:
    #         start_grid = Grid(inners[unittype][0], inners[unittype][1])
    #     else:
    #         start_grid = Grid(s[0], s[1])
    #     end_grid = Grid(e[0], e[1]) 
    # if CarSetting.behavior_type == 3 :
    #     s = walkables[random.randint(0, len(walkables)//3)]
    #     e = walkables[random.randint(len(walkables)//3, len(walkables)-1)]
    #     start_grid = Grid(s[0], s[1])
    #     end_grid = Grid(e[0], e[1]) 


    # 搜索街区终点
    result_grid = mycar_walking(start_grid, end_grid, generated_map)
    # 回溯街区路径
    path = []
    while result_grid is not None:
        path.append(Grid(result_grid.x, result_grid.y))
        result_grid = result_grid.parent
    ALL_PATHS.append(path)
    abel_score = 0
    # 输出街区和路径，路径用星号表示
    for i in range(0, len(generated_map)):
        for j in range(0, len(generated_map[0])):
            if contain_grid(path, i, j):
                # star = colored('*', 'magenta', attrs=['reverse', 'blink'])
                # print(star +", ", end="")
                cprint('*'+", ","green",attrs=['reverse', 'blink'],end = "")
                abel_score += 1
            else:
                if generated_map[i][j] == 1:
                    cprint('1'+", ","grey",attrs=['reverse', 'blink'],end = "")
                else:
                    print(str(generated_map[i][j]) + ", ", end="")
        print()
    print('abel_score=', abel_score)
    return abel_score

def visual_to_png(res):
    # res = [[0.01, 0.9, 0.46], [0.64, 0.24, 1], [0.87, 0.99, 0.47]]
    # fig, ax = plt.subplots(figsize=(15,15)
    colormap = pyplot.cm.cubehelix_r
    fig, ax = plt.subplots()
    ax = sns.heatmap(res, cmap=colormap)
    # plt.yticks(rotation=0,fontsize=16);
    # plt.xticks(fontsize=12);
    # plt.tight_layout()
    plt.title('Heatmap of citytype vs car-district-type', fontsize = 20) # title with fontsize 20
    plt.xlabel('car-district-type', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('citytype', fontsize = 15) # y-axis label with fontsize 1
    plt.savefig('i1colorlist.png')

def hotmap(allpaths):
    # res = [[0.01, 0.9, 0.46], [0.64, 0.24, 1], [0.87, 0.99, 0.47]]
    # fig, ax = plt.subplots(figsize=(15,15)
    generated_map = unit_types[0]
    for path in allpaths:
        for i in range(0, len(generated_map)):
            for j in range(0, len(generated_map[0])):
                if contain_grid(path, i, j):
                    energy_consume = 1
                    if generated_map[i][j] == 2:
                        energy_consume *= 1.5
                    elif generated_map[i][j] == 3:
                        energy_consume *= 1.6


                    heats[i][j] += energy_consume

    for i in range(0, len(generated_map)):
        for j in range(0, len(generated_map[0])):
            if heats[i][j] == 0:
                # 应该是封闭区间或者是道路的周边，需要进行差值法
                if i != 0 and i!= len(generated_map) -1 and j!=0 and j<= len(generated_map) -2:
                    heats[i][j] = (heats[i-1][j] + heats[i+1][j] + heats[i][j-1] + heats[i][j+1])/2
            print(str(heats[i][j]) + ", ", end="")
        print()
    colormap = pyplot.cm.cubehelix_r
    fig, ax = plt.subplots()
    ax = sns.heatmap(heats, cmap=colormap)
    # plt.yticks(rotation=0,fontsize=16);
    # plt.xticks(fontsize=12);
    # plt.tight_layout()
    plt.title('Heatmap of station most needed', fontsize = 20) # title with fontsize 20
    plt.xlabel('x', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('y', fontsize = 15) # y-axis label with fontsize 1
    plt.savefig('i4heatmap.png')


def main():

    show_img("resources/i1geographical_urban.jpg")
    time.sleep(3)



    simulate_num = 160

    mycarly_types = [None, None, None, None]

    mycarly_types[0] = int(simulate_num * 0.35)
    mycarly_types[1] = int(simulate_num * 0.30)
    mycarly_types[2] = int(simulate_num * 0.20)
    mycarly_types[3] = int(simulate_num * 0.15)

    print('mycarly_types=', mycarly_types)
    mydict = {}
    visual_data = []
    for i in range(len(unit_types)):
        print('city_types =', i, '\n')
        generated_map = unit_types[i]
        for mycarly_type in range(len(mycarly_types)):
            car_setting = CarSetting(mycarly_type)
            car_setting.myprint()
            scores = []
            for j in range(mycarly_types[mycarly_type]):
                score = single_turn(i, generated_map, car_setting)
                scores.append(score)
                # time.sleep(random.uniform(0.1, 0.8))
            mydict[i, mycarly_type] = scores

    print('\n'*3)

    welcome = colored('#'*10+' This statistics:'+'#'*10, 'red', attrs=['reverse', 'blink'])
    print(welcome, '\n')
    time.sleep(0.5)
    for i in range(len(unit_types)):
        type_data = []
        for mycarly_type in range(len(mycarly_types)):
            print('city type ', i, ' with mycar_type ', mycarly_type, 
                    ' simulate scores:', mydict[i, mycarly_type])
            x = round(statistics.mean(mydict[i, mycarly_type]), 2)
            # 数据的总体方差
            p = round(statistics.pvariance(mydict[i, mycarly_type]), 2)
            print(colored('mean simulate scores =','red'), x)
            print(colored('pvariance simulate scores =','blue'), p)
            type_data.append(x)
            # time.sleep(random.uniform(0.1, 0.5))
        visual_data.append(type_data)
    # print('#'*50,ALL_PATHS)
    
    # visual_to_png(type_data)
    i2simulator.main(visual_data)
    hotmap(ALL_PATHS)


if __name__ == "__main__":
    main()


