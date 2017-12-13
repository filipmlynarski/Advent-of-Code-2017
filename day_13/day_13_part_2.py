puzzle = open('puzzle').read().splitlines()

firewall = [0 for i in range(int(puzzle[-1].split(':')[0]) + 1)]
for i in puzzle:
	firewall[int(i.split(':')[0])] = int(i.split()[-1])
delay = -1

while True:
	delay += 1
	for idx, i in enumerate(firewall):
		if i != 0 and (idx + delay) % (i*2 - 2) == 0: break
	else: break

print delay