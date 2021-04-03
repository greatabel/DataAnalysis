import simpy

def resource_user(env, resource):
	request = resource.request()
	yield request
	yield env.timeout(1)
	print('do something take 1 time') 
	resource.release(request)


env = simpy.Environment()
res = simpy.Resource(env, capacity=1)
user = env.process(resource_user(env, res))
env.run()