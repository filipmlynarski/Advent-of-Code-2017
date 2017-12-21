import numpy as np

def change(x):
	ret = {}
	for j in x:
		ret[j[0]] = np.array([int(i) for i in j[3:-2].split(',')])
	return ret

puzzle = open('puzzle').read().splitlines()
particles = {}

for idx, i in enumerate(puzzle):
	i += ','
	i = i.split()
	particles[idx] = change(i)

for i in range(400):
	closest = []

	for i in particles:
		particles[i]['v'] += particles[i]['a']
		particles[i]['p'] += particles[i]['v']
		closest.append(sum(abs(particles[i]['p'])))
	
	closest_idx = closest.index(min(closest))

print closest_idx