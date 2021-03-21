'''
For the call center in Exercise 16 of Chap. 4, the arrival rate is not actually a steady 60/h, 
it varies throughout the day. Data on call counts, by hour, for 1 month (31 days) 
can be found on the book website in CallCounts.xls. Use these data to estimate arrival 
rates for a piecewise-constant, nonstation- ary Poisson arrival process. 
Implement this arrival process in your call center simulations. Does this affect your recommendation?
'''

'''
问题1和问题2的区别在于到达率,使用细化方法为每个客户生成非平稳到达时间，然后使用基于事件的方法来运行模拟
我直接把表格数据取出一部分，作为1小时内到达的数量，进行重复多次模拟

'''
from SimPy.Simulation import * 
from random import expovariate,seed

## Model components ------------------------

class Source(Process):
    """ Source generates customers randomly"""

    def generate(self,number,interval,resource,mon):       
        for i in range(number):
            c = Customer(name = "Customer%02d"%(i,))
            activate(c,c.visit(b=resource,M=mon))          
            t = expovariate(1.0/interval)
            yield hold,self,t

class Customer(Process):
    """ Customer arrives, is served and leaves """
        
    def visit(self,b,M):       
        arrive = now()
        yield request,self,b
        wait = now()-arrive
        M.observe(wait)                                
        tib = expovariate(1.0/timeInBank)
        yield hold,self,tib
        yield release,self,b
 
## Experiment data -------------------------

maxNumber = 100
maxTime = 2000.0  # minutes                                    
timeInBank = 60.0   # mean, minutes
ARRint = 5.0     # mean, minutes
Nc = 7            # number of counters
theSeed = 393939

## Model  ----------------------------------

def model(runSeed=theSeed, maxNumber=maxNumber):                            
    seed(runSeed)
    k = Resource(capacity=Nc,name="Clerk")  
    wM = Monitor()                                   

    initialize()
    s = Source('Source')
    activate(s,s.generate(number=maxNumber,interval=ARRint, 
                          resource=k,mon=wM),at=0.0)         
    simulate(until=maxTime)
    return (wM.count(),wM.mean())                     

## Experiment/Result  ----------------------------------
sum_clerk = 0
# 使用其中一天的测试数据，要使用整个的excel数据，以此类推
theseeds = [27,37,58,68,65,33,37,21]         
for Sd in theseeds:
    result = model(Sd, Sd)
    print("Callcenter Served %3d calls was %6.2f clients."% result  )
    
    t = result[1] * 1.05
    
    print('after agents will not be experts across all products, need', t)
    sum_clerk += t
print('average need clerk=',sum_clerk/8)
# average clerk= 42.292041748298864
