import time
import simpy

# https://simpy.readthedocs.io/en/latest/topical_guides/real-time-simulations.html
def example(env):
    start = time.perf_counter()
    yield env.timeout(1)
    end = time.perf_counter()
    print('Duration of one simulation time unit: %.2fs' % (end - start))
env = simpy.Environment()
proc = env.process(example(env))
env.run(until=proc)

print('-'*20, 'realtime')
import simpy.rt
env = simpy.rt.RealtimeEnvironment(factor=0.1)
proc = env.process(example(env))
env.run(until=proc)