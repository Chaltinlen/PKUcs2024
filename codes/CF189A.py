a = [0, 0, 0]
n, a[0], a[1], a[2] = map(int, input().split())
cut = [0 for i in range(n+1)]
for i in range(3):
	if a[i] <= n:
		cut[a[i]] = 1
for i in range(3):
	for j in range(n - a[i] + 1):
		if cut[j] != 0:
			cut[j + a[i]] = max(cut[j + a[i]], cut[j] + 1)
print(cut[n])