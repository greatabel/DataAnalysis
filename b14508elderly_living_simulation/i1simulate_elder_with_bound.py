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
from my_unittype import unit_types, bathrooms, beds
from elderly import OldMan


def elder_walking(start, end, generated_map=[]):
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
            if generated_map[i][j] == 0:
                walkables.append([i, j])
    return walkables


def single_turn(unittype, generated_map, oldman):
    walkables = all_walkable(generated_map)
    # welcome = colored('#'*10+' This turn generated_map:'+'#'*10, 'red', attrs=['reverse', 'blink'])
    # print(welcome, '\n')
    print('-'*10, 'run new simulation turn', '-'*10, '\n')
    # 设置起点和终点
    start_grid = Grid(2, 1)
    end_grid = Grid(2, 5)
    if oldman.behavior_type == 0 :
        s = walkables[random.randint(0, len(walkables)/2)]
        e = walkables[random.randint(len(walkables)/2, len(walkables)-1)]
        start_grid = Grid(s[0], s[1])
        end_grid = Grid(e[0], e[1])   
    if oldman.behavior_type == 1:
        s = walkables[random.randint(0, len(walkables)/2)]
        e = walkables[random.randint(len(walkables)/2, len(walkables)-1)]
        start_grid = Grid(s[0], s[1])
        end_grid = Grid(2, 8)   
    if oldman.behavior_type == 2:
        s = walkables[random.randint(0, len(walkables)/2)]
        e = walkables[random.randint(len(walkables)/2, len(walkables)-1)]
        start_grid = Grid(beds[unittype][0], beds[unittype][1])
        end_grid = Grid(e[0], e[1]) 
    if oldman.behavior_type == 3 :
        s = walkables[random.randint(0, len(walkables)//3)]
        e = walkables[random.randint(len(walkables)//3, len(walkables)-1)]
        start_grid = Grid(s[0], s[1])
        end_grid = Grid(e[0], e[1]) 
    # 搜索房间终点
    result_grid = elder_walking(start_grid, end_grid, generated_map)
    # 回溯房间路径
    path = []
    while result_grid is not None:
        path.append(Grid(result_grid.x, result_grid.y))
        result_grid = result_grid.parent

    abel_score = 0
    # 输出房间和路径，路径用星号表示
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
    plt.title('Heatmap of unittype vs elderly-type', fontsize = 20) # title with fontsize 20
    plt.xlabel('elderly-type', fontsize = 15) # x-axis label with fontsize 15
    plt.ylabel('unittype', fontsize = 15) # y-axis label with fontsize 1
    plt.savefig('colorlist.png')


def main():


    simulate_num = 40

    elderly_types = [None, None, None, None]
    # living room type
    '''
    类型一：客厅型老人：以看电视为主，占比70%左右；
    类型二：外出型老人：为外出活动为主，占比20%左右；
    类型三：卧室型老人：以卧床休息为主，占比5%左右；
    类型四：家务型老人：以进行家务行为为主，占比较小。

    '''
    elderly_types[0] = int(simulate_num * 0.7)
    elderly_types[1] = int(simulate_num * 0.2)
    elderly_types[2] = int(simulate_num * 0.05)
    elderly_types[3] = int(simulate_num * 0.05)

    print('elderly_types=', elderly_types)
    mydict = {}
    visual_data = []
    for i in range(len(unit_types)):
        print('unit_types =', i, '\n')
        generated_map = unit_types[i]
        for elderly_type in range(len(elderly_types)):
            oldman = OldMan(elderly_type)
            oldman.myprint()
            scores = []
            for j in range(elderly_types[elderly_type]):
                score = single_turn(i, generated_map, oldman)
                scores.append(score)
                time.sleep(random.uniform(0.1, 0.5))
            mydict[i, elderly_type] = scores

    print('\n'*3)

    welcome = colored('#'*10+' This statistics:'+'#'*10, 'red', attrs=['reverse', 'blink'])
    print(welcome, '\n')
    time.sleep(0.5)
    for i in range(len(unit_types)):
        type_data = []
        for elderly_type in range(len(elderly_types)):
            print('unit type ', i, ' with elderly_type ', elderly_type, 
                    ' simulate scores:', mydict[i, elderly_type])
            x = round(statistics.mean(mydict[i, elderly_type]), 2)
            # 数据的总体方差
            p = round(statistics.pvariance(mydict[i, elderly_type]), 2)
            print(colored('mean simulate scores =','red'), x)
            print(colored('pvariance simulate scores =','blue'), p)
            type_data.append(x)
            time.sleep(random.uniform(0.1, 0.5))
        visual_data.append(type_data)
    visual_to_png(visual_data)



if __name__ == "__main__":
    main()


