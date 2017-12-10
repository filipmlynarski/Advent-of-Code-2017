puzzle = open('puzzle').read()
lengths = [int(i) for i in puzzle.split(',')]
sizes = [i for i in range(256)]

skip = 0
idx = 0
for i in lengths:
	if idx+i > len(sizes):
		to_reverse = sizes[idx:] + sizes[:(idx+i)%len(sizes)]
		to_reverse = to_reverse[::-1]
		sizes[idx:] = to_reverse[:len(sizes[idx:])]
		sizes[:(idx+i)%len(sizes)] = to_reverse[len(sizes[idx:]):]
	else:
		to_reverse = sizes[idx: idx+i]
		to_reverse = to_reverse[::-1]
		sizes[idx: idx+i] = to_reverse
	idx = (idx+i+skip)%len(sizes)
	skip += 1

print sizes[0] * sizes[1]