puzzle = open('puzzle').read().splitlines()

puzzle = [int(i) for i in puzzle]
i, j = 0, 0

while i < len(puzzle):
	puzzle[i] += 1
	i += puzzle[i] - 1
	j += 1

print j