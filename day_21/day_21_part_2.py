import numpy as np

puzzle = open('puzzle').read().splitlines()
grid = np.array([list(i) for i in '.#./..#/###'.split('/')])

def compare(x, y):
	for i in range(4):
		if (x == y).all():
			return True
		elif (np.flip(x, 0) == y).all() or (np.flip(x, 1) == y).all():
			return True
		x = np.rot90(x)
	return False


def find_match(x):
	for i in puzzle:
		if i.split()[0][len(x)] == '/':
			to_check = np.array([list(j) for j in i.split()[0].split('/')])
			if compare(x, to_check):
				return np.array([list(j) for j in i.split()[-1].split('/')])
	return False

for i in range(18):
	if len(grid) % 2 == 0:
		new_grid = np.chararray((len(grid) / 2 * 3, len(grid) / 2 * 3))
		for y in range((len(grid) / 2)):
			for x in range((len(grid) / 2)):
				test = grid[y*2: (y+1) * 2, x*2: (x+1) * 2]
				new_grid[y*3: (y+1) * 3, x*3: (x+1) * 3] = find_match(test)
	else:
		new_grid = np.chararray((len(grid) / 3 * 4, len(grid) / 3 * 4))
		for y in range((len(grid) / 3)):
			for x in range((len(grid) / 3)):
				test = grid[y*3: (y+1) * 3, x*3: (x+1) * 3]
				new_grid[y*4: (y+1) * 4, x*4: (x+1) * 4] = find_match(test)
	grid = new_grid

print sum([str((''.join(i)).replace('#', '1').replace('.', '0')).count('1') for i in grid.tolist()])