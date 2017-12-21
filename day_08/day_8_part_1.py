import operator
puzzle = open('puzzle').read().splitlines()

saved = {}
for i in puzzle:
	i = i.split()
	adding = i[:3]
	statement = i[4:]
	which = statement[0]
	if not which in saved:
		saved[which] = 0
	statement[0] = 'saved["' + which + '"]'
	if eval(" ".join(statement)):
		if not adding[0] in saved:
			saved[adding[0]] = 0
		if adding[1] == 'inc':
			saved[adding[0]] += int(adding[2])
		elif adding[1] == 'dec':
			saved[adding[0]] -= int(adding[2])
print saved[max(saved.iteritems(), key=operator.itemgetter(1))[0]]