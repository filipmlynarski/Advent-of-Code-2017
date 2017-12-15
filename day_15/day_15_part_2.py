A = 289
B = 629
pairs = 0

for i in range(5000000):
	while True:
		A = A * 16807 % 2147483647
		if A % 4 == 0: break
	while True:
		B = B * 48271 % 2147483647
		if B % 8 == 0: break

	if str(bin(A))[-16:] == str(bin(B))[-16:]:
		pairs += 1

print pairs