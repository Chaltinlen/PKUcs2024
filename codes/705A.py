n = int(input())
for i in range(n):
	if i >= 1:
		print("that", end = " ")
	if not i % 2:
		print("I hate", end = " ")
	if i % 2:
		print("I love", end = " ")

print("it")