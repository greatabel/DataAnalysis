"""
Consider the call arrival data from the previous exercise. Let N(t) 
repre- sent the cumulative number of arrivals by time t. 
If the process is nonsta- tionary Poisson then Var(N(t))/E(N(t)) = 1 for all t, 
or stated differently Var(N(t)) = βE(N(t)) with β = 1. Since you have arrival count data, 
you can estimate Var(N(t)) and E(N(t)) at t = 1,2,...,8 h. 
Use these data to fit the regression model Var(N(ti)) = βE(N(ti)) and see if the estimated value of β 
supports the choice of a nonstationary Poisson arrival process. Hints: This
is regression through the origin. Also, remember that N(ti) represents the total
number of arrivals by time ti.
"""

'''
从𝐸(𝛽)和q3图 感觉不像是柏松分布，，我认为β的估计值不支持非平稳泊松到达过程的选择。

'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mymean = []

call_data = pd.read_excel("q2/CallCounts.xls", sheet_name="Sheet1", na_values="n/a")


mean_1 = np.mean(call_data["8AM-9AM"])
var_1 = np.var(call_data["8AM-9AM"])
mymean.append(var_1 / mean_1)

mean_2 = np.mean(call_data["8AM-9AM"] + call_data["9AM-10AM"])
var_2 = np.var(call_data["8AM-9AM"] + call_data["9AM-10AM"])
mymean.append(var_2 / mean_2)

mean_3 = np.mean(call_data["8AM-9AM"] + call_data["9AM-10AM"] + call_data["10AM-11AM"])
var_3 = np.var(call_data["8AM-9AM"] + call_data["9AM-10AM"] + call_data["10AM-11AM"])
mymean.append(var_3 / mean_3)

print("-" * 20)
print("np.mean(mymean), as 𝐸(𝛽)=", np.mean(mymean))


plt.figure(figsize=(10, 8))
x = call_data.columns[0:3]

y1 = [mean_1, mean_2, mean_3]
y2 = [var_1, var_2, var_3]
l1 = plt.plot(x, y1, "r--", label="mean")
l2 = plt.plot(x, y2, "g--", label="var")
plt.plot(x, y1, "ro-", x, y2, "g+-")
plt.legend()
plt.savefig("q3.png")
# 结果：
# np.mean(mymean), as 𝐸(𝛽)= 0.8743966313506735
