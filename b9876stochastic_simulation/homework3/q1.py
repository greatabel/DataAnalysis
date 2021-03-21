"""
Problem 1. (20 Pts.) Exercise 16 from Chapter 4 of the textbook.


Software Made Personal (SMP) customizes software products in two areas: financial tracking and contact management.
 They currently have a customer support call center that handles technical questions for owners of their software 
 from the hours of 8 a.m. to 4 p.m. Eastern time.
When a customer calls, they first listen to a recording that asks them to se- lect among the product lines; 
historically 59% are financial products and 41% contact management products. 
The number of customers who can be connected (talking to an agent or on hold) at any one time is essentially unlimited. 
Each product line has its own agents. If an appropriate agent is available then the call is immediately routed to the agent; 
if an appropriate agent is not available, then the caller is placed in a hold queue (and listens to a combination of music and ads). 
SMP has observed that hang-ups very rarely happen.
SMP is hoping to reduce the total number of agents they need by cross- training agents so that they can answer calls for any product line. 
Since the agents will not be experts across all products, this is expected to increase the time to process a call by about 5%. 
The question that SMP has asked you to answer is how many cross-trained agents 
are needed to provide service at the same level as the current system.
Incoming calls can be modeled as a Poisson arrival process with a rate of 60 per hour. The mean time required for 
an agent to answer a question is 5 min, 
with the actual time being Erlang-2 for financial calls, and Erlang-3 for contact management calls. 
The current assignment of agents is four for financial and three for contact management. 
Simulate the system to find out how many agents are needed to deliver the same level of service 
in the cross-trained system as in the current system.

"""

'''
我觉得抽象出来 这是一个 M / G / s系统刺激具有不同数量服务器的交叉训练系统
然后进行多轮模拟，得出数据结论
'''
import random, math
import numpy as np
import SimPy.Simulation as Sim

from SimPy.Simulation import *

from random import expovariate, seed
## Model components ------------------------

class Source(Process):
    """ Source generates customers randomly """

    def generate(self,number,meanTBA,resource):     
        for i in range(number):
            c = Customer(name = "Customer%02d"%(i,))
            activate(c,c.visit(timeInBank=5.0,
                               res=resource))          
            # t = expovariate(1.0/meanTBA)
            t = 5
            yield hold,self,t

class Customer(Process):
    """ Customer arrives, is served and  leaves """
        
    def visit(self,timeInBank,res):       
        arrive = now()       # arrival time        
        print ("%8.3f %s: Here I am     "%(now(),self.name) )

        yield request,self,res                       
        wait = now()-arrive  # waiting time        
        print ("%8.3f %s: Waited %6.3f"%(now(),self.name,wait) )
        yield hold,self,timeInBank               
        yield release,self,res                     
        
        print ("%8.3f %s: Finished      "%(now(),self.name) )

## 测试实验数据-------------------------

maxNumber = 100       # 设置100模拟1小时足够了，根本不会有100个人来                               
maxTime = 60.0  # minutes                                
ARRint = 5.0    # mean, minutes，间隔，平均一个人服务5分钟
k = Resource(name="Counter",unitName="Clerk")     

## Model/Experiment ------------------------------
seed(99999)
initialize()
s = Source('Source')
activate(s,s.generate(number=maxNumber,            
                      meanTBA=ARRint, resource=k),at=0.0)        
simulate(until=maxTime)

print('we can see 12 customers served by old ways by 4 financial 3 management')
# 原来是7个人，不考虑金融和管理占用时间不同，新的都值上升了0.05的时间，于是换算下：
print((4+3)*(1+0.05), ' now we need 8 clerk')