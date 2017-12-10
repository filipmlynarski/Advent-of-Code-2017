puzzle = open('puzzle').read().splitlines()

def total_weight(x):
	ret = 0
	for dsc in x:
		for i in puzzle:
			i = [t.split(',')[0] for t in i.split()]
			if dsc == i[0]:
				ret += int(i[1][1:-1])
				if '->' in i:
					ret += total_weight(i[3:])
				break
	return ret

s = {}
for i in puzzle:
	i = [t.split(',')[0] for t in i.split()]
	if '->' in i:
		save = []
		for j in i[3:]:
			save.append(total_weight([j]))
		if min(save) != max(save):
			if len(s.keys()) == 0 or save[0] < s[s.keys()[0]]:
				s = {}
				for idx, c in enumerate(i[3:]):
					s[c] = save[idx]

mx = max(s, key=s.get)
mn = min(s, key=s.get)

for i in puzzle:
	if i.startswith(mx):
		print int(i.split()[1][1:-1]) - (s[mx] - s[mn])