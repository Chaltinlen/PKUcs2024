k = int(input())
mis = list(map(int, input().split()))
length = [0 for i in range(k)]
length[k-1] = 1
for i in range(k-2, -1, -1):
	maximum = 0
	for j in range(i, k):
		if mis[j] <= mis[i]:
			maximum = max(maximum, length[j])
	length[i] = maximum + 1
print(max(length))
