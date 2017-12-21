puzzle = open('puzzle').read().splitlines()
ret = 0

for i in puzzle:
	i = i.split()
	for j in i:
		if i.count(j) != 1:
			break
	else:
		ret += 1
print ret