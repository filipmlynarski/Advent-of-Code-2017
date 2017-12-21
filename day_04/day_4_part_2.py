puzzle = open('puzzle').read().splitlines()
ret = 0

def compare(x, y):
	for i in x:
		if y.count(i) != x.count(i): return False
	return True

for i in puzzle:
	i = i.split()
	bad = False
	for x in range(len(i)):
		for y in range(x+1, len(i)):
			if len(i[x]) == len(i[y]):
				if compare(i[x], i[y]):
					bad = True
	if not bad: ret += 1
print ret