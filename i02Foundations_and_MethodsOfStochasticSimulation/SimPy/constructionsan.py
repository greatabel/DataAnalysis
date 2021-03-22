# -*- coding: utf-8 -*-
# Example 3.3 (Construction project).
# ===================================
#
# A construction project consists of a large number of activities. Some of these can be completed in parallel (drywall can be ordered while the foundation is being poured), while some cannot commence until others are
# completed (the roof cannot be constructed until the framing is finished). Since the
# durations of the activities are not precisely predictable, the project planners would
# like to take into account this variability when bidding the project because there will
# be penalties for completing the project after the contract date.

# Maximum Path Simulation of the SAN
# ----------------------------------
#
# 1. set s = 0
# 2. repeat $n$ times:
#   1. generate $X1 , X2 , . . . , X5$
#   2. set $Y =$ max$(X1 + X4 , X1 + X3 + X5 , X2 + X5)$
#   3. if $Y > t_p$ then set $s = s + 1$
# 3. estimate $\theta$ by $\hat{\theta} = s/n$

import math, random

# Initialization
class SAN:
    N =  1000
    tp = 5.0

# <codecell>

def constructionsan(seed):
    random.seed(seed)
    X = [random.expovariate(1./1.0) for i in range(5)]
    Y = max(X[0]+X[3], X[0]+X[2] + X[4], X[1] + X[4])
    return Y

# <codecell>

initialseed = 2124
Y = [constructionsan(initialseed + i) for i in range(SAN.N)]
Ytp = [1.0 if Y[i]>SAN.tp else 0 for i in range(SAN.N)]
thetahat = sum(Ytp)/SAN.N
sethetahat = math.sqrt((thetahat*(1-thetahat))/SAN.N)

# Compare to
#
# $Pr\left(Y ≤ t_p\right) = \left(\frac{1}{2} t_p^2 − 3 t_p − 3\right) e^{−2t_p} + \left(−\frac{1}{2} t_p^2 − 3t_p + 3\right) e^{-t_p} + 1 − e^{−3t_p}$
#

Theta = 1 - ( (math.pow(SAN.tp,2) / 2 - 3.0 * SAN.tp - 3) * math.exp(-2 * SAN.tp) \
    + (-1.0/2 *math.pow(SAN.tp, 2) - 3 * SAN.tp + 3) * math.exp(-SAN.tp) + 1.0 - math.exp(-3 * SAN.tp))

# Compare $\hat{\theta}$ from simulation with true value $\theta$ and checking that it is within the standard error $\hat{se}$

print("Compare (thetahat = %6.5f) plus/minus 1.96 * (sehat = %6.5f) to theta = %6.5f" %
      (thetahat, sethetahat, Theta))
lowerlimit = (thetahat - 1.96 * sethetahat)
upperlimit = (thetahat + 1.96 * sethetahat)
print("(%4.3f, %4.3f) %4.3f" % (lowerlimit, upperlimit, Theta))

# $\theta$ is within $\pm 1.96 \hat{se}$ of $\hat{\theta}$

import matplotlib.pyplot as plt
plt.hist(Y, bins = 60, range = (0, 12), histtype = 'step', cumulative=True)
