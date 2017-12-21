puzzle = open('puzzle').read().splitlines()

ret = 0
for i in puzzle:
	i=i.split()
	i = [int(i) for i in i]
	for x in range(len(i)):
		for y in range(len(i)):
			if x != y:
				if int(float(i[x]) /i[y]) == float(float(i[x]) /i[y]):
					ret += i[x] /i[y]
print ret
