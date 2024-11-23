N, B = map(int, input().split())
p = list(map(int, input().split()))
w = list(map(int, input().split()))
maximum = [0 for j in range(B+1)]
for i in range(N):
	for j in range(B, w[i]-1, -1):
		maximum[j] = max(maximum[j], maximum[j-w[i]] + p[i])
print(max(maximum))