maks = 1
inp = 277678

while maks**2 < inp:
	maks += 2
grid = [[1 for i in range(maks)] for j in range(maks)]
x = maks/2
y = maks/2
center = [x, y]
done = 1

for i in range(maks/2):
	to_do = (i*2 + 3)**2 - done
	done = (i*2 + 3)**2
	quarter = to_do/4
	for j in range(to_do):
		old = grid[x][y]
		if j / quarter == 0:
			if j == 0:
				y += 1
			else:
				x -= 1
		elif j / quarter == 1:
			y -= 1
		elif j / quarter == 2:
			x += 1
		elif j / quarter == 3:
			y += 1
		grid[x][y] = old + 1
		if grid[x][y] == inp:
			print abs(x - center[0]) + abs(y - center[1])