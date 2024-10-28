n = int(input())
a = []
x = 0
for i in range(n):
	a = [int(num) for num in input().split()]
if a[0] == a[1]:
	x = a[0]
	for i in range(2, n):
		if i != x:
			print(str(i + 1))
else:
	if a[0] != a[2]:
		print("1")
	else:
		print("2")