A = 289
B = 629
pairs = 0

for i in range(40000000):
	A = A * 16807 % 2147483647
	B = B * 48271 % 2147483647

	if str(bin(A))[-16:] == str(bin(B))[-16:]:
		pairs += 1

print pairs