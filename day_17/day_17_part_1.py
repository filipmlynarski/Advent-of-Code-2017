nmnbrs = [0]
idx = 0
steps = 303

for i in range(1, 2018):
	idx = (idx + steps) % len(nmnbrs) + 1
	nmnbrs.insert(idx, i)
print nmnbrs[idx + 1]