puzzle = open('puzzle').read().splitlines()
puzzle = [i.split() for i in puzzle]

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

registers1 = {str(i[1]): 0 for i in puzzle if not RepresentsInt(i[1])}
registers1['p'] = 0
registers1['que'] = []
idx1 = 0

registers2 = {str(i[1]): 0 for i in puzzle if not RepresentsInt(i[1])}
registers2['p'] = 1
registers2['que'] = []
idx2 = 0

sent = 0

while True:
	while idx1 < len(puzzle):
		i = puzzle[idx1]
		if i[0] == 'snd':
			if RepresentsInt(i[1]):
				registers2['que'].append(int(i[1]))
			else:
				registers2['que'].append(registers1[i[1]])

		elif i[0] == 'set':
			if RepresentsInt(i[2]):
				registers1[i[1]] = int(i[2])
			else:
				registers1[i[1]] = registers1[i[2]]

		elif i[0] == 'add':
			if RepresentsInt(i[2]):
				registers1[i[1]] += int(i[2])
			else:
				registers1[i[1]] += registers1[i[2]]

		elif i[0] == 'mul':
			if RepresentsInt(i[2]):
				registers1[i[1]] *= int(i[2])
			else:
				registers1[i[1]] *= registers1[i[2]]

		elif i[0] == 'mod':
			if RepresentsInt(i[2]):
				registers1[i[1]] %= int(i[2])
			else:
				registers1[i[1]] %= registers1[i[2]]

		elif i[0] == 'rcv':
			if len(registers1['que']) > 0:
				registers1[i[1]] = registers1['que'].pop(0)
			else:
				break
				idx1 -= 1

		elif i[0] == 'jgz':
			if RepresentsInt(i[1]):
				if int(i[1]) > 0:
					if RepresentsInt(i[2]):
						idx1 += int(i[2]) - 1
					else:
						idx1 += registers1[i[2]] - 1
			elif registers1[i[1]] > 0:
				if RepresentsInt(i[2]):
					idx1 += int(i[2]) - 1
				else:
					idx1 += registers1[i[2]] - 1
		idx1 += 1
	
	else:
		break

	if len(registers2['que']) == 0:
		break

	while idx2 < len(puzzle):
		i = puzzle[idx2]
		if i[0] == 'snd':
			sent += 1
			if RepresentsInt(i[1]):
				registers1['que'].append(int(i[1]))
			else:
				registers1['que'].append(registers2[i[1]])

		elif i[0] == 'set':
			if RepresentsInt(i[2]):
				registers2[i[1]] = int(i[2])
			else:
				registers2[i[1]] = registers2[i[2]]

		elif i[0] == 'add':
			if RepresentsInt(i[2]):
				registers2[i[1]] += int(i[2])
			else:
				registers2[i[1]] += registers2[i[2]]

		elif i[0] == 'mul':
			if RepresentsInt(i[2]):
				registers2[i[1]] *= int(i[2])
			else:
				registers2[i[1]] *= registers2[i[2]]

		elif i[0] == 'mod':
			if RepresentsInt(i[2]):
				registers2[i[1]] %= int(i[2])
			else:
				registers2[i[1]] %= registers2[i[2]]

		elif i[0] == 'rcv':
			if len(registers2['que']) > 0:
				registers2[i[1]] = registers2['que'].pop(0)
			else:
				break
				idx2 -= 1

		elif i[0] == 'jgz':
			if RepresentsInt(i[1]):
				if int(i[1]) > 0:
					if RepresentsInt(i[2]):
						idx2 += int(i[2]) - 1
					else:
						idx2 += registers2[i[2]] - 1
			elif registers2[i[1]] > 0:
				if RepresentsInt(i[2]):
					idx2 += int(i[2]) - 1
				else:
					idx2 += registers2[i[2]] - 1
		idx2 += 1
	
	else:
		break

	if len(registers1['que']) == 0:
		break

print sent