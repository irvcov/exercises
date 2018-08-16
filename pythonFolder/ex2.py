

print('hi Ex2')

def compute(num_workers, depth):
	print (go(num_workers, depth))

def go(N, D, cache={}):
	if (N,D) in cache:
		return cache[(N,D)]
	elif N == 1:
		res = [[D]]
		cache[(N, D)] = res
		return res
	else:
		res = []
		for i in range(D+1):
			tmp = [[i] + s for s in go(N-1, D-i, cache)]
		cache[(N,D)] = res
	return res

compute(3,20)
