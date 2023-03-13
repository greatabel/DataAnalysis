import csv
import random
import string
from datetime import datetime, timedelta

# 生成时间序列
start_date = datetime(2021, 1, 1, 0, 0, 0)
end_date = datetime(2022, 12, 31, 23, 0, 0)
time_series = [start_date + timedelta(hours=i) for i in range(int((end_date - start_date).total_seconds() / 3600) + 1)]

# 生成每天的demand记录
data = []
daily_demand_totals = []
for day in range((end_date - start_date).days + 1):
    demand_total = 0
    num_records = random.randint(1, 50)
    for i in range(num_records):
        max_demand = 1240 - demand_total if i == num_records - 1 else 1240
        if max_demand < 0:
            max_demand = 0
        demand = random.randint(0, max_demand)
        order_movement_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=18))
        record_number_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
        vin = ''.join(random.choices(string.ascii_uppercase + string.digits, k=17))
        batch_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        data.append((time_series[day*24+i], demand, order_movement_id, record_number_id, vin, batch_number))
        demand_total += demand
    daily_demand_totals.append((start_date + timedelta(days=day), demand_total))

# 写入数据到CSV文件
with open('data/records.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'demand', 'Order Movement ID', 'record number id', 'VIN', 'Batch Number'])
    writer.writerows(data)

with open('data/daily_demand_totals.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'demand'])
    for day, demand_total in enumerate(daily_demand_totals):
        writer.writerow([demand_total[0], demand_total[1]])
