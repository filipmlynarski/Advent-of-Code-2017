puzzle = open('puzzle').read().splitlines()

ret = 0
for i in puzzle:
	i=i.split()
	i = [int(i) for i in i]
	ret += max(i) - min(i)
print ret
