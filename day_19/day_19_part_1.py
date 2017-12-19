puzzle = open('puzzle').read().splitlines()
x, y = [puzzle[0].index(i) for i in puzzle[0] if i != ' '][0], 0
collected = []
directon = [0, 1]
while True:
	last = [x, y]
	x += directon[0]
	y += directon[1]

	if puzzle[y][x] not in [' ', '|', '+', '-']:
		collected.append(puzzle[y][x])
	
	if y == len(puzzle) or y == 0 or x == len(puzzle[0]) or x == 0:
		break

	elif puzzle[y][x] == '+':
		to_check = []

		if y == 0:
			to_check.append([x, y+1])
		elif y == len(puzzle) - 1:
			to_check.append([x, y-1])
		else:
			to_check.append([x, y-1])
			to_check.append([x, y+1])

		if x == 0:
			to_check.append([x+1, y])
		elif x == len(puzzle[0]) - 1:
			to_check.append([x-1, y])
		else:
			to_check.append([x-1, y])
			to_check.append([x+1, y])

		for i in to_check:
			if puzzle[i[1]][i[0]] != ' ' and last != i:
				directon = [i[0] - x, i[1] - y]
				break

	elif puzzle[y][x] == ' ':
		break

print ''.join(collected)