import numpy as np
import scipy
import matplotlib.pyplot as plt
import math

limit = 1000000

# comment out folling  line, just for test
limit = 100

def uniform_proposal(x, delta=2.0):
    return np.random.uniform(x - delta, x + delta)


saved = []
def q4(p, nsamples, proposal=uniform_proposal):
    x = 1 # start somewhere

    for i in range(nsamples):
        trial = proposal(x) # random neighbour from the proposal distribution
        acceptance = p(trial)/p(x)
        f = 1 - math.pow((2/x),3 )
        print('acceptance=', acceptance, f)

        # accept the move conditionally
        if np.random.uniform() < acceptance:
            x = trial

        if acceptance > 0.95:
        	saved.append(x)
        yield x

def cauchy(x, mu, gamma):
    return 1./(np.pi*gamma*(1.+((x-mu)/gamma)**2))

p = lambda x: cauchy(x, -2, 0.5)


samples = list(q4(p, limit))
print('part a ' ,samples)

print('part b ', saved)