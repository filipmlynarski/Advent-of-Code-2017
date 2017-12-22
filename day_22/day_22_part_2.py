puzzle = open('puzzle').read().splitlines()

infected = {}

for y in range(len(puzzle)):
	for x in range(len(puzzle[y])):
		if puzzle[y][x] == '#':
			infected[str(y) + ',' + str(x)] = 2

y, x = len(puzzle)/2, len(puzzle[0])/2
direction = 2
send = 0

for i in range(10000000):
	try:
		infected[str(y) + ',' + str(x)] += 1
		
		if infected[str(y) + ',' + str(x)] == 1:
			direction = (direction - 1) % 4

		elif infected[str(y) + ',' + str(x)] == 2:
			send += 1

		elif infected[str(y) + ',' + str(x)] == 3:
			direction = (direction + 1) % 4

		elif infected[str(y) + ',' + str(x)] == 4:
			infected[str(y) + ',' + str(x)] = 0
			direction = (direction + 2) % 4

	except:
		infected[str(y) + ',' + str(x)] = 1
		direction = (direction - 1) % 4

	if direction == 0:
		y += 1
	elif direction == 1:
		x -= 1
	elif direction == 2:
		y -= 1
	elif direction == 3:
		x += 1

print send