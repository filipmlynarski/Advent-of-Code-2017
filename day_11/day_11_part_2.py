puzzle = open('puzzle').read().split(',')

x, y = 0, 0
save = []
for move in puzzle:
	move_by = 1
	if len(move) == 1:
		move_by = 2
	if 'n' in move:
		y += move_by
	elif 's' in move:
		y -= move_by
	if 'e' in move:
		x += move_by
	elif 'w' in move:
		x -= move_by
	save.append([x, y])
furthest = 0
for idx, i in enumerate(save):
	x = i[0]
	y = i[1]
	x2, y2 = 0, 0
	moves = 0
	while True:
		moves += 1
		if y2 > y:
			y2 -= 1
			if x2 > x:
				x2 -= 1
			elif x2 < x:
				x2 += 1
			else:
				y2 -= 1
		elif y2 < y:
			y2 += 1
			if x2 > x:
				x2 -= 1
			elif x2 < x:
				x2 += 1
			else:
				y2 += 1
		elif x2 > x:
			x2 -= 1
		elif x2 < x:
			x2 += 1
		if x==x2 and y==y2: break
	if moves > furthest:
		furthest = moves
print furthest