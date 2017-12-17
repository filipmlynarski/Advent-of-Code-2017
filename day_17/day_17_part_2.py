after = 0
idx = 0
steps = 303

for i in range(1, 50000001):
	idx = (idx + steps)%i + 1
	if idx==1: after = i

print after