m = int(input())
x = [[] for i in range(m)]
for j in range(0, m):
	x[j] = [int(num) for num in input().split()]
for j in range(0, m):
	if x[j][0] + x[j][1] + x[j][2] + x[j][3] == 24 or x[j][0] + x[j][1] + x[j][2] - x[j][3] == 24 or x[j][0] + x[j][1] - x[j][2] + x[j][3] == 24 or x[j][0] + x[j][1] - x[j][2] - x[j][3] == 24	or x[j][0] - x[j][1] + x[j][2] + x[j][3] == 24 or x[j][0] - x[j][1] + x[j][2] - x[j][3] == 24 or x[j][0] - x[j][1] - x[j][2] + x[j][3] == 24 or x[j][0] - x[j][1] - x[j][2] - x[j][3] == 24 or -x[j][0] + x[j][1] + x[j][2] + x[j][3] == 24 or -x[j][0] + x[j][1] + x[j][2] - x[j][3] == 24 or -x[j][0] + x[j][1] - x[j][2] + x[j][3] == 24 or -x[j][0] + x[j][1] - x[j][2] - x[j][3] == 24	or -x[j][0] - x[j][1] + x[j][2] + x[j][3] == 24 or -x[j][0] - x[j][1] + x[j][2] - x[j][3] == 24 or -x[j][0] - x[j][1] - x[j][2] + x[j][3] == 24 or -x[j][0] - x[j][1] - x[j][2] - x[j][3] == 24:
		print("YES")
	else:
		print("NO")