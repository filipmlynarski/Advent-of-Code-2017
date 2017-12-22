puzzle = open('puzzle').read().splitlines()
infected = []

for y in range(len(puzzle)):
	for x in range(len(puzzle[y])):
		if puzzle[y][x] == '#':
			infected.append([y, x])
y, x = len(puzzle)/2, len(puzzle[0])/2

direction = 2
send = 0

for i in range(10000):
	if [y, x] in infected:
		infected.pop(infected.index([y, x]))
		direction = (direction + 1) % 4
	else:
		send += 1
		infected.append([y, x])
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