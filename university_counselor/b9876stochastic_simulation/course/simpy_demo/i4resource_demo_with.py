import simpy

def resource_user(env, resource):
	with  resource.request() as req:
		yield req
		yield env.timeout(1)
		print('do something take 1 time') 



env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
user = env.process(resource_user(env, res))
env.run()