puzzle = open('puzzle').read().splitlines()

firewall = [0 for i in range(int(puzzle[-1].split(':')[0]) + 1)]
for i in puzzle:
	firewall[int(i.split(':')[0])] = int(i.split()[-1])

caught = 0

for idx, i in enumerate(firewall):
	if i != 0 and (idx) % (i*2 - 2) == 0:
		caught += idx * i

print caught
