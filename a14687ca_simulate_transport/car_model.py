import random


def init_car_model(cell_temp, leng, cell2, way, auto_p, car_p):
    if cell_temp[way][0] == 0:
        leng[way] = leng[way] + 1
        if random.randint(1, 100) <= car_p *(1- auto_p) * 100:
            cell_temp[way][0] = 1  # people's car
        elif random.randint(1, 100) <= car_p *auto_p * 100:
            cell_temp[way][0] = 2  # auto car
    cell2[way][0] = random.randint(0, 2)
