puzzle = open('puzzle').read()
count = 0

result = []
result2 = []
score = 0

for i in range(128):
	lengths = [ord(i) for i in puzzle + '-' + str(i)] + [17, 31, 73, 47, 23]
	sizes = [i for i in range(256)]

	skip = 0
	idx = 0

	for loop in range(64):
		for i in lengths:
			if idx+i > len(sizes):
				to_reverse = sizes[idx:] + sizes[:(idx+i)%len(sizes)]
				to_reverse = to_reverse[::-1]
				sizes[idx:] = to_reverse[:len(sizes[idx:])]
				sizes[:(idx+i)%len(sizes)] = to_reverse[len(sizes[idx:]):]
			else:
				to_reverse = sizes[idx: idx+i]
				to_reverse = to_reverse[::-1]
				sizes[idx: idx+i] = to_reverse
			idx = (idx+i+skip)%len(sizes)
			skip += 1

	result = []
	for i in range(16):
		result.append(sizes[16*i])
		for j in range(16*i+1, 16*(i+1)):
			result[-1] ^= sizes[j]

	def my_hex(x):
		basic = hex(i).split('x')[-1]
		return (not (len(basic) -1 )) * '0' + basic

	result2.append([my_hex(i) for i in result])
	result2[-1] = ''.join(result2[-1])
	result2[-1] = bin(int(result2[-1], 16))[2:]

	score += result2[-1].count('1')

print score