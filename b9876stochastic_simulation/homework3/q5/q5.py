import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
headers = ['Imaging duration','Deviation from appointment']
df = pd.read_csv('Problem5_Data.csv',names=headers)
print (df)

# df['Date'] = df['Date'].map(lambda x: datetime.strptime(str(x), '%Y/%m/%d %H:%M:%S.%f'))
x = df['Imaging duration']
y = df['Deviation from appointment']

# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

#可以打开plt.show()
# plt.show()
print('a. normal distribution , We can see from iamge')
print('b. We can just use total random per hour to simulate arrivals')

from SimPy.Simulation import *
from random import expovariate, seed  # 1

# Model components ------------------------

print('c. coding is below.')
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
c = Customer(name="Test")
t = expovariate(1.0 / 5.0)  # 3
activate(c, c.visit(timeInBank), at=t)  # 4
simulate(until=maxTime)