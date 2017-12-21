import numpy as np

def change(x):
	ret = {}
	for j in x:
		ret[j[0]] = np.array([int(i) for i in j[3:-2].split(',')])
	return ret

puzzle = open('puzzle').read().splitlines()
particles = []

for idx, i in enumerate(puzzle):
	i += ','
	i = i.split()
	particles.append(change(i))

for i in range(100):
	for i in range(len(particles)):
		particles[i]['v'] += particles[i]['a']
		particles[i]['p'] += particles[i]['v']

	while True:
		positions = [str(i['p']) for i in particles]

		for i in particles:
			occurs = np.where(np.array(positions) == str(i['p']))[0]

			if len(occurs) > 1:
				for j in occurs[::-1]:
					positions.pop(j)
					particles.pop(j)
				break

		else:
			break

print len(particles)