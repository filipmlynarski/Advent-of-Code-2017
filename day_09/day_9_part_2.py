import json

puzzle = list(open('puzzle').read())
garbage= 0

while '!' in puzzle:
	idx = puzzle.index('!')
	puzzle.pop(idx + 1)
	puzzle.pop(idx)

while '<' in puzzle:
	idx = puzzle.index('<')
	i = 1
	while True:
		if puzzle[idx + i] == '>':
			garbage += i-1
			puzzle = puzzle[:idx] + puzzle[idx + i + 1:]
			break
		i += 1

print garbage