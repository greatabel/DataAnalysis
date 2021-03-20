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

import random, math
import numpy as np
import SimPy.Simulation as Sim

from SimPy.Simulation import *


## Experiment data -------------------------
evarge_sevice_time = 5
maxNumber = 5
maxTime = 60.0  # minutes
ARRint = 1.0  # time between arrivals, minutes

## Model/Experiment ------------------------------

class Source(Process):
    """ Source generates customers regularly """

    def generate(self, number, TBA):
        for i in range(number):
            c = Customer(name="Customer%02d" % (i,))
            activate(c, c.visit(timeInBank=evarge_sevice_time))
            yield hold, self, TBA


class Customer(Process):
    """ Customer arrives, looks around and leaves """

    def visit(self, timeInBank):
        print("%7.4f %s: I am calling" % (now(), self.name))
        yield hold, self, timeInBank
        print("%7.4f %s: I finished calling" % (now(), self.name))






initialize()
s = Source()
activate(s, s.generate(number=maxNumber, TBA=ARRint), at=0.0)
simulate(until=maxTime)
