puzzle = open('puzzle').read().splitlines()

for i in puzzle:
	i = [t.split(',')[0] for t in i.split()]
	if '->' in i:
		for j in puzzle:
			j = j.split()
			j = [t.split(',')[0] for t in j]
			if '->' in j and i[0] in j and i != j:
				break
		else:
			print i[0]