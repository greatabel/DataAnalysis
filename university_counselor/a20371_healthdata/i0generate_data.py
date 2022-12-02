import csv
import random


def main():
    # 年龄,BMI,饮酒 ,心脏病,糖尿病
    first_row = ['age','bmi','drink','heart_disease','diabetes','patient_id', 'sex', 'painloc', 'painexer', 'relrest']
    # first_row = ["barometric_value","humidity","ultraviolet_rays","average_quality","ozone_relative","record_id","pm1","pm2","pm3","pm4"]

    rows = []
    rows.append(first_row)
    patient_id = 1
    for i in range(1000000*4):
    # for i in range(1000*5):
        age = random.randint(60, 90)
        if age > 80:
            age = age  - random.randint(0, 10)
        bmi = random.randint(10, 30)
        if bmi > 15:
            bmi += random.randint(0, 3)
            age += random.randint(0, 10)
        drink = random.randint(0, 1)
        heart_disease = random.randint(0, 1)
        diabetes = random.randint(0, 1)

        patient_id += 1
        sex = 0
        if random.randint(0, 100) > 52:
            sex = 0
        else:
            sex = 1

        painloc = random.randint(0, 1)
        painexer = random.randint(0, 1)
        relrest = random.randint(0, 1)

        if age > 70:
            if random.randint(0, 1) == 0 and drink == 1:
                heart_disease = 1
        if age > 80:
            if random.randint(0, 1) == 0 and drink == 1:
                diabetes = 1
        
        row = [age, bmi, drink, heart_disease, diabetes, patient_id, sex, painloc, painexer, relrest]
        rows.append(row)

    print('len(rows)=',len(rows))
    with open('mydata/my_health_data.csv', 'w') as myfile:
    # with open('mydata/my_wheather_data.csv', 'w') as myfile:

        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

        for r in rows:
            wr.writerow(r)


main()