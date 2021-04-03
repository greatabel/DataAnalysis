import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

'''
q4_generate_a, q4_generate_b 是生成需要随机数据的函数，
具体情况可以修改limit的数值，在不同数据规模进行实验
'''
limit = 1000000

# comment out folling  line, just for test
limit = 100


def uniform_proposal(x, delta=2.0):
    return np.random.uniform(x - delta, x + delta)


S = []


def cauchy(x, mu, gamma):
    return 1.0 / (np.pi * gamma * (1.0 + ((x - mu) / gamma) ** 2))


p = lambda x: cauchy(x, -2, 0.5)




def q4_generate_a():
    r = []
    for i in range(0, limit):

        u = np.random.uniform()
        d = pow(1 - u, 1 / 3)
        x = 2 / d
        r.append(x)
    return r


samples = q4_generate_a()

print("\npart a samples=", samples)

print("\npart b ")



def q4_generate_b():
    for i in range(limit):
        ss = []
        for j in range(10):
            u = np.random.uniform()
            d = pow(1 - u, 1 / 3)
            x = 2 / d
            ss.append(x)
        S.append(np.cumsum(ss)[-1])

q4_generate_b()
p = np.cumsum(np.array(S) > 40)[-1] / limit
print("P(S10 > 40)=", p)
lb = p - 1.96 * np.sqrt(p * (1 - p) / limit)
ub = p + 1.96 * np.sqrt(p * (1 - p) / limit)
print("estimate and a 95% CI using "+limit +" samples.")
print(lb, ub)
