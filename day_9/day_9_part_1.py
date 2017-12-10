import json
puzzle = list(open('puzzle').read())

while '!' in puzzle:
	idx = puzzle.index('!')
	puzzle.pop(idx + 1)
	puzzle.pop(idx)

while '<' in puzzle:
	idx = puzzle.index('<')
	i = 1
	while True:
		if puzzle[idx + i] == '>':
			puzzle = puzzle[:idx] + puzzle[idx + i + 1:]
			break
		i += 1

def find_depth(p, d):
	ret = []
	idx = 0
	while idx < len(p):
		exit = 0
		if p[idx] == '{':
			idx2 = idx
			occur = False
			while idx2 < len(p):
				idx2 += 1
				if p[idx2] == '{':
					occur = True
					exit += 1
				elif p[idx2] == '}':
					if exit == 0:
						break
					exit -= 1
			ret.append(d)
			if occur:
				ret.extend(find_depth(p[idx+1:idx2], d+1))
			idx = idx2
		idx += 1
	return ret

print sum(find_depth(puzzle, 1))