import numpy as np
import random
import copy
import matplotlib.pyplot as plt


from car_model import init_car_model



def move(way):
    for j in range(0, width-1):
        if j==0 and cell[way][0]!=0:
            x = 0
            for i in range(j+1,j+4):
                if cell[way][i]!=0:
                    x=1
            if x==0:
                cell_temp[way][1]=cell_temp[way][0]
                cell_temp[way][0]=0
                cell2[way][1] = cell2[way][0]
                cell2[way][0] = -1
        elif cell[way][j]!=0:
            if cell2[way][j] == way:
                cell2[way][j] = -1
            if cell2[way][j] != -1 and cell_temp[way][j] == 1:
                a = change_way(way, j)
                if a ==0:
                    continue
            elif cell2[way][j] != -1 and cell_temp[way][j] == 2 and j+5+way>width:
                a = change_way(way, j)
                if a == 0:
                    continue
            x = 0
            for i in range(j+1,min(j+3,width-1)):
                if cell[way][i]!=0:
                    x=1
            if x==0:
                if  j+3<width-4 and cell[way][j+3]== 0 and cell_temp[way][j]==1 and random.randint(1,100)<=20:
                        cell_temp[way][j+2]=cell_temp[way][j]
                        cell_temp[way][j] = 0
                        cell2[way][j + 2] = cell2[way][j]
                        cell2[way][j] = 0
                        k = j+2
                else:
                    cell_temp[way][j+1]=cell_temp[way][j]
                    cell_temp[way][j]=0
                    cell2[way][j + 1] = cell2[way][j]
                    cell2[way][j] = 0
                    k=min(j+1,width-2)
                if cell_temp[way][k]==1:
                    if random.randint(1,100)<=5 and cell_temp[way][k-1]==0:
                        cell_temp[way][k-1]=1
                        cell_temp[way][k]=0
                        cell2[way][k - 1] = cell2[way][k]
                        cell2[way][k] = -1
                    elif random.randint(1,100)<=5 and cell_temp[way][k+1]==0:
                        cell_temp[way][k + 1] = 1
                        cell_temp[way][k] = 0
                        cell2[way][k + 1] = cell2[way][k]
                        cell2[way][k] = -1


def remove(way):
    if cell_temp[way][width-1] != 0 and cell2[way][width-1]==-1:
        leng[3] = leng[3]+1
        leng[way] = leng[way] -1
        cell_temp[way][width-1]=0


def change_way(way, local):
    m = 0
    n = 0
    if way ==1:
        if cell2[way][local] != way:
            for i in range(local-3,min(local+4,width-1)):
                if cell[cell2[way][local]][i] != 0:
                    m = 1
            if m == 0:
                cell_temp[cell2[way][local]][local+1]=cell_temp[way][local]
                cell_temp[way][local] = 0
                leng[way]=leng[way]-1
                leng[cell2[way][local]] = leng[cell2[way][local]]+1
                cell2[cell2[way][local]][local+1] = -1
                cell2[cell2[way][local]][local] = 0
        if m == 0:
            return 0
        else:
            return 1
    if way == 0:
        if cell2[way][local] != way:
            for i in range(local-3,min(local+4,width-1)):
                if cell[1][i] != 0:
                    m = 1
            if m == 0:
                cell_temp[1][local+1]=cell_temp[way][local]
                cell_temp[way][local] = 0
                leng[way]=leng[way]-1
                leng[1] = leng[1]+1
                cell2[1][local + 1] = cell2[way][local]
                cell2[way][local] = 0
        if m == 0:
            return 0
        else:
            return 1
    if way == 2:
        if cell2[way][local] != way:
            for i in range(local - 3, min(local + 4,width-1)):
                if cell[1][i] != 0:
                    m = 1
            if m == 0:
                cell_temp[1][local + 1] = cell_temp[way][local]
                cell_temp[way][local] = 0
                leng[way] = leng[way] - 1
                leng[1] = leng[1] + 1
                cell2[1][local + 1] = cell2[way][local]
                cell2[way][local] = 0
        if m == 0:
            return 0
        else:
            return 1


if __name__ == '__main__':
    length = 3
    width = 200
    d = 0
    cell = np.zeros((length,width),int)
    cell_temp = copy.deepcopy(cell)
    cell2 = copy.deepcopy(cell)
    for i in range(0, length):
        for j in range(0,width):
            cell_temp[i][j] = 0
    for i in range(0, length):
        for j in range(0,width):
            cell2[i][j] = -1
    #cell_temp[i][1] = 1
    #cell_temp[i][2] = 1
    global leng
    leng = {0: 0, 1: 0, 2: 0, 3: 0}
    list1 = []
    # for i in range(0, 100):
    for i in range(0, 5):
        print('i', '='*10, i)
        while True:
            if d % 4 == 0:
                init_car_model(cell_temp, leng, cell2,  0, i/100, 0.3)
            if d % 3 == 0:
                init_car_model(cell_temp, leng, cell2, 1, i/100, 0.3)
            if d % 5 == 0:
                init_car_model(cell_temp, leng, cell2, 2, i/100, 0.3)
            cell = copy.deepcopy(cell_temp)
            # 显示每一轮的图像
            plt.imshow(cell)
            plt.pause(0.0000000001)
            move(0)
            move(1)
            move(2)
            remove(0)
            remove(1)
            remove(2)
            d = d + 1
            # if leng[3] >= 2000:
            if leng[3] >= 5:
                list1.append(d)
                d=0
                leng[3]=0
                break
            print('len(list1)=', len(list1))
            print('leng[3]=', leng[3])

    print(list1)

    # plt.show(block=False)
    # plt.pause(0.2)

    x = np.arange(0, 1, 0.2)
    # x = np.arange(0, 1, 0.01)

    plt.close()

    plt.plot(x, list1)
    plt.savefig('result_comparison.png')
    plt.show()
    # plt.pause(5)

