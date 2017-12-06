puzzle = open('puzzle').read().splitlines()

puzzle = [int(i) for i in puzzle]
i, j = 0, 0

while i < len(puzzle):
	x = i
	i += puzzle[i]
	if i < len(puzzle):
		if puzzle[x] >= 3:
			puzzle[x] -= 1
		else:
			puzzle[x] += 1
	j += 1

print j