def around(x, y):
	ret = 0
	values = [x - 1, y - 1, x + 1, y + 1]
	for idx, i in enumerate(values):
		if i < 0:
			values[idx] += 1
		elif i >= len(grid):
			values[idx] -= 1
	for i in range(values[0], values[2] + 1):
		for j in range(values[1], values[3] + 1):
			ret += grid[i][j]
	return ret

inp = 277678
grid = [[1]]
done = False

while not done:
	grid.insert(0, [0 for i in range(len(grid[0]))])
	grid.append([0 for i in range(len(grid[0]))])
	for i in range(len(grid)):
		grid[i].insert(0,0)
		grid[i].append(0)
	x, y = len(grid)-2, len(grid)-2
	quarter = len(grid)-1
	for j in range(len(grid) ** 2 - (len(grid)-2) ** 2):
		old = grid[x][y]
		if j / quarter == 0:
			if j == 0:
				y = y + 1
			else:
				x = x - 1
		elif j / quarter == 1:
			y = y - 1
		elif j / quarter == 2:
			x = x + 1
		elif j / quarter == 3:
			y = y + 1
		grid[x][y] = around(x, y)
		if grid[x][y] > inp:
			print grid[x][y]
			done = True
			break