x = int(input())
y = 0
while x != 1:
	if x % 2 == 0:
		y = x // 2
		print(f"{x}/2={y}")
	else:
		y = 3*x + 1
		print(f"{x}*3+1={y}")
	x, y = y, x
