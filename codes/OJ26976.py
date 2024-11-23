n = int(input())
*nums, = map(int, input().split())
length = [[1 for i in range(n)] for j in range(2)]
for i in range(n):
	for j in range(i+1, n):
		if nums[j] > nums[i]:
			length[0][j] = max(length[1][i] + 1, length[0][j])
		elif nums[j] < nums[i]:
			length[1][j] = max(length[0][i] + 1, length[1][j])
print(max(length[1][n-1], length[0][n-1]))
