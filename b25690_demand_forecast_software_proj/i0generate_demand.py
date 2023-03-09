import csv
import random
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
        data.append((time_series[day*24+i], demand))
        demand_total += demand
    daily_demand_totals.append(demand_total)

# 写入数据到CSV文件
with open('data/records.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'demand'])
    writer.writerows(data)

with open('data/daily_demand_totals.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['date', 'demand'])
    for day, demand_total in enumerate(daily_demand_totals):
        writer.writerow([start_date + timedelta(days=day), demand_total])