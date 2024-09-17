n = int(input())
x = 0
for i in range(n):
	operate = list(input())[1]
	if operate == "+":
		x += 1
	else:
		x -= 1
print(str(x))