from copy import deepcopy	

puzzle = [1, 0, 14, 14, 12, 12, 10, 10, 8, 8, 6, 6, 4, 3, 2, 1]
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
		print count
		break
	seen.append(changed)
	puzzle = changed