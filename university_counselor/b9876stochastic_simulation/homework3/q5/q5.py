import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

headers = ['Imaging duration','Deviation from appointment']
df = pd.read_csv('Problem5_Data.csv',names=headers)
# print (df)

# df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S.%f'))
x = df['Imaging duration']
y = df['Deviation from appointment']

# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()
plt.savefig("q5.png")
#可以打开plt.show()
# plt.show()
print('a. normal distribution , We can see from iamge')
print('b. 从问题（a）中，我选择正态分布以产生偏差，因此到达时间为约会时间+导数 \
 我设置时间从 时间0 开始，当第一个客户到来时，时间是S1，第二个客户到来的时间是S2，依此类推。\
 两个客户之间的间隔时间为Ai，即60 +偏差。 最后，当第i位来宾到达时，Si = Si-1 + Ai。使用此递归公式，我可以模拟约会驱动的到达')

from SimPy.Simulation import *
from random import expovariate, seed  # 1

# Model components ------------------------

print('c. coding is below.')

def CI95(data):
    a = np.array(data)
    n = len(a)
    m = np.mean(a)
    sd = np.std(a,ddof=1)
    h = 1.96*sd / np.sqrt(n)
    return m, [m-h,m+h]

class Customer(Process):
    """ Customer arrives at a random time,
        looks around and then leaves """

    def visit(self, timeInBank):
        print("%f %s Here I am" % (now(), self.name))
        yield hold, self, timeInBank
        print("%f %s I must leave" % (now(), self.name))

# Experiment data -------------------------


maxTime = 100.0    # minutes
timeInBank = 10.0
# Model/Experiment ------------------------------

seed(99999)  # 2
initialize()
for i in range(10):
	c = Customer(name="Test"+str(i))
	t = expovariate(1.0 / 5.0)  # 3
	activate(c, c.visit(timeInBank), at=t)  # 4
	simulate(until=maxTime)

print('CI95 =', CI95([700, 801, 745]))