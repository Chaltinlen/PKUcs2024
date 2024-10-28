n = int(input())
trees = [list(map(int, input().split())) for i in range(n)]
cnt = min(2, n)
for i in range(1, n-1):
	if trees[i][0] - trees[i-1][0] > trees[i][1]: 
		cnt += 1
	elif trees[i+1][0] - trees[i][0] > trees[i][1]:
		trees[i][0] += trees[i][1]
		cnt += 1
print(cnt)