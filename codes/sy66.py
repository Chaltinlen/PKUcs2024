n = int(input())
if n == 2:
	print("*\n**")
	exit()
for i in range(n - 1):
	print("*", end = "")
	if i == 0:
		print()
		continue
	for j in range(i-1):
		print(" ", end = "")
	print("*")
for k in range(n):
	print("*", end = "")