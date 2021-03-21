'''
Consider the call arrival data from the previous exercise. Let N(t) 
repre- sent the cumulative number of arrivals by time t. 
If the process is nonsta- tionary Poisson then Var(N(t))/E(N(t)) = 1 for all t, 
or stated differently Var(N(t)) = βE(N(t)) with β = 1. Since you have arrival count data, 
you can estimate Var(N(t)) and E(N(t)) at t = 1,2,...,8 h. 
Use these data to fit the regression model Var(N(ti)) = βE(N(ti)) and see if the estimated value of β 
supports the choice of a nonstationary Poisson arrival process. Hints: This
is regression through the origin. Also, remember that N(ti) represents the total
number of arrivals by time ti.
'''
