import math
n = int(input())
factor = []
if n == 1:
	print("1")
else:
	for i in range(2, 1 + int(math.sqrt(n))):
		if n % i == 0:		
			n /= i
			if n % i == 0:
				print("0")
				exit()
			factor.append(i)
		if n == 1:
			break
	if n > 1:
		factor.append(n)
	if not factor or len(factor) % 2 == 1:
		print("-1")
	else:
		print("1")