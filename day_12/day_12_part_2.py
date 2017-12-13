puzzle = [i.split() for i in open('puzzle').read().replace(',', ' ').replace(' <->', ' ').splitlines()]

groups = 0

while puzzle:
	groups += 1
	match = puzzle[0]
	puzzle.pop(0)

	while True:
		for idx, i in enumerate(puzzle):
			if i[0] in match:
				for to_check in i[1:]:
					if not to_check in match:
						match.append(to_check)
				puzzle.pop(idx)
				break
		else:
			break
print groups
