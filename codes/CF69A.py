n = int(input())
x, y, z = 0, 0, 0
x_sum, y_sum, z_sum = 0, 0, 0
for i in range(n):
	x, y, z = list(map(int, input().split()))
	x_sum += x
	y_sum += y
	z_sum += z

if x_sum == 0 and y_sum == 0 and z_sum == 0:
	print("YES")
else:
	print("NO")
