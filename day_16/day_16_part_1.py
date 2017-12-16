puzzle = open('puzzle').read()
dancers = [chr(i) for i in range(ord('a'), ord('p') + 1)]

for i in puzzle.split(','):
	if i[0] == 's':
		dancers = dancers[-int(i[1:]):] + dancers[:-int(i[1:])]
	elif i[0] == 'x':
		fast = i[1:].split('/')
		dancers[int(fast[0])], dancers[int(fast[1])] = dancers[int(fast[1])], dancers[int(fast[0])]
	elif i[0] == 'p':
		fast = i[1:].split('/')
		one = dancers.index(fast[0])
		two = dancers.index(fast[1])
		dancers[one], dancers[two] = dancers[two], dancers[one]

print ''.join(dancers)