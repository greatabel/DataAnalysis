import csv
import random
import math
from datetime import datetime, timedelta


def demand_pattern(hour):
    # 日间和夜间的需求变化
    day_demand = 0.7 * math.sin((hour - 6) * math.pi / 12) + 0.3
    return day_demand

def week_pattern(day):
    # 工作日和周末的需求变化
    if day % 7 == 5 or day % 7 == 6:
        return 0.8
    else:
        return 1.0

# 生成时间序列
start_date = datetime(2020, 1, 1, 0, 0, 0)
end_date = datetime(2022, 12, 31, 23, 0, 0)
time_series = [start_date + timedelta(hours=i) for i in range(int((end_date - start_date).total_seconds() / 3600) + 1)]

# 生成每天的demand记录
data = []
daily_demand_totals = []
for day in range((end_date - start_date).days + 1):
    demand_total = 0
    for hour in range(24):
        # 在基本需求值的基础上，根据小时和星期调整需求
        base_demand = 1000
        demand = int(base_demand * demand_pattern(hour) * week_pattern(day))
        
        # 加入一定的随机扰动
        demand += random.randint(-10, 10)
                # 确保需求值不为负
        demand = max(0, demand)

        data.append((time_series[day * 24 + hour], demand))
        demand_total += demand
    daily_demand_totals.append(demand_total)

# 写入数据到CSV文件
with open('../b25690_demand_forecast_software_proj/data/records.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'demand'])
    writer.writerows(data)

with open('../b25690_demand_forecast_software_proj/data/daily_demand_totals.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['timestamp', 'demand'])
    for day, demand_total in enumerate(daily_demand_totals):
        writer.writerow([start_date + timedelta(days=day), demand_total])
