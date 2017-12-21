from copy import deepcopy	

puzzle = open('puzzle').read().splitlines()
puzzle = [int(i) for i in puzzle[0].split()]
seen = [puzzle]

def change(x):
	mx = max(x)
	idx = x.index(mx)
	x[idx] = 0
	for i in range(1, mx+1):
		x[(idx+i)%len(x)] += 1
	return x

count = 0
while 1:
	changed = change(deepcopy(puzzle))
	count += 1
	if changed in seen:
		print changed
		print count
		break
	seen.append(changed)
	puzzle = changed