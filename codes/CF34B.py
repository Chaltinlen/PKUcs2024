n, m = map(int, input().split())
tv = sorted(list(map(int, input().split())))
ans = 0
for i in range(m):
	if tv[i] >= 0:
		break
	ans += tv[i]
print(-ans)
