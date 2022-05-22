import csv
import random


def main():
    # 年龄,BMI,饮酒 ,心脏病,糖尿病
    row = [66,18.9,0,1,1]

    rows = []
    for i in range(1000):
        age = random.randint(60, 90)
        bmi = random.randint(10, 30)
        drink = random.randint(0, 1)
        heart_disease = random.randint(0, 1)
        diabetes = random.randint(0, 1)
        if age > 70:
            if random.randint(0, 1) == 0 and drink == 1:
                heart_disease = 1
        if age > 80:
            if random.randint(0, 1) == 0 and drink == 1:
                diabetes = 1
        row = [age, bmi, drink, heart_disease, diabetes ]
        rows.append(row)

    print('len(rows)=',len(rows))
    with open('data/mydata.csv', 'w') as myfile:

        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for r in rows:
            wr.writerow(r)


main()