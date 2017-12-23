puzzle = open('puzzle').read().splitlines()
puzzle = [i.split() for i in puzzle]

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

registers = {str(i[1]): 0 for i in puzzle if not RepresentsInt(str(i[1]))}
registers['a'] = 1
idx = 0
save = 0

while idx < len(puzzle):
	i = puzzle[idx]
	if puzzle[idx][0] == 'set':
		if RepresentsInt(i[2]):
			registers[i[1]] = int(i[2])
		else:
			registers[i[1]] = registers[i[2]]

	elif puzzle[idx][0] == 'sub':
		if RepresentsInt(i[2]):
			registers[i[1]] -= int(i[2])
		else:
			registers[i[1]] -= registers[i[2]]

	elif puzzle[idx][0] == 'mul':
		save += 1
		if RepresentsInt(i[2]):
			registers[i[1]] *= int(i[2])
		else:
			registers[i[1]] *= registers[i[2]]

	elif puzzle[idx][0] == 'jnz':
		if RepresentsInt(i[1]):
			if int(i[1]) != 0:
				if RepresentsInt(i[2]):
					idx += int(i[2]) - 1
				else:
					idx += registers[i[2]] - 1
		elif registers[i[1]] != 0:
			if RepresentsInt(i[2]):
				idx += int(i[2]) - 1
			else:
				idx += registers[i[2]] - 1

	idx += 1

print registers['h']