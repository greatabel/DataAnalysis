import csv
import random


def main():
    # 年龄,BMI,饮酒 ,心脏病,糖尿病
    first_row = ['age','bmi','drink','heart_disease','diabetes']

    rows = []
    rows.append(first_row)
    for i in range(1000000*5):
        age = random.randint(60, 90)
        if age > 80:
            age = age  - 10
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
    with open('mydata/my_health_data.csv', 'w') as myfile:

        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for r in rows:
            wr.writerow(r)


main()