import numpy as np
from scipy.linalg import expm, logm, inv, pinv
from random import random
from SimPy.Simulation import *

'''
我实现了不同阶段的模型类，用户来访的通用类

'''
class PhaseModel(object):
    
    def __init__(self, phase_type_generator, initial_state):
        self.phases = initial_state.shape[1]
        self.number_of_parameters = 2 * self.phases - 1
        self.phase_type_generator = phase_type_generator
        self.initial_state = initial_state
        self.e = np.ones((self.phases , 1))
        self.exit_rate_vector = - phase_type_generator.dot(self.e)
        
    def _pdf(self, y):  
        return self.initial_state.dot(expm(self.phase_type_generator * y)).dot(self.exit_rate_vector).reshape(-1)
    
    def pdf(self, data):
        return np.array([self._pdf(i) for i in data])

    def _cdf(self, y):  
        return 1 - self.initial_state.dot(expm(self.phase_type_generator * y)).dot(self.e).reshape(-1)

    def sample(self): 
        s = 0
        for i in range(self.phases - 1):
            total_transition_rate = self.phase_type_generator[i, i + 1] + self.exit_rate_vector[i]
            time_until_transition = np.random.exponential(1 / total_transition_rate)
            s += time_until_transition
            if random() < self.exit_rate_vector[i] / total_transition_rate:
                return s
        time_until_transition = np.random.exponential(1 / self.exit_rate_vector[-1])
        s += time_until_transition
        return s
        
    def log_likelyhood(self, data):
        probs = self.pdf(data)
        log_prob = np.log(probs[~np.isnan(probs)])
        return log_prob.sum()

    def aic(self, data):
        return 2 * self.number_of_parameters - 2 * self.log_likelyhood(data)





class Customer(Process):
    """ Customer arrives, looks around and leaves """

    def visit(self, timeInBank):
        print("%7.4f %s: Here I am" % (now(), self.name))  # 1
        yield hold, self, timeInBank
        print("%7.4f %s: I must leave" % (now(), self.name))  # 2

# Experiment data -------------------------


maxTime = 400.0  # minutes                                   #3

# Model/Experiment ------------------------------

initialize()

c1 = Customer(name="Klaus")  # 4
activate(c1, c1.visit(timeInBank=10.0), at=5.0)
c2 = Customer(name="Tony")
activate(c2, c2.visit(timeInBank=7.0), at=2.0)
c3 = Customer(name="Evelyn")
activate(c3, c3.visit(timeInBank=20.0), at=12.0)  # 5

simulate(until=maxTime)  