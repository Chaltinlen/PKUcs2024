
import math

n = int(input())
for i in range(n):
	a, b, c = map(float, input().split())
	delta = b**2 - 4 * a * c
	x_symmetry = - b / (2*a)
	if delta == 0:
		print("x1=x2=", end = "")
		x_symmetry = str(format(x_symmetry, ".5f"))
		if b == -0:
			print("0.00000")
		else:
			print(str(x_symmetry))
	elif delta > 0:
		x_delta = math.sqrt(delta)/(2*a)
		print("x1=", end = "")
		x1 = str(format(x_symmetry+x_delta, ".5f"))
		if x1 == "-0.00000":
			print("0.00000", end = "")
		else:
			print(x1, end = "")
		print(";x2=",end = "")
		x2 = str(format(x_symmetry-x_delta, ".5f"))
		if x2 == "-0.00000":
			print("0.00000")
		else:
			print(x2)
	else:
		x_symmetry = str(format(x_symmetry, ".5f"))
		x_delta = format(math.sqrt(-delta) / (2 * a), ".5f")
		
		print("x1=", end = "")
		if b == -0:
			print("0.00000", end = "")
		else:
			print(x_symmetry, end = "")
		print("+"+str(x_delta)+"i;x2=", end = "")
		if b == -0:
			print("0.00000", end = "")
		else:
			print(x_symmetry, end = "")
		print("-"+str(x_delta)+"i")
		'''

import math
n = int(input())
for i in range(n):
    a, b, c = map(float, input().split())
    if b == 0:
        b = -b
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        x1 = format(x1, ".5f")
        x2 = format(x2, ".5f")
        print(f"x1={x1};x2={x2}")
    elif delta == 0:
        t = (-b) / (2 * a)
        x1 = format(t, ".5f")
        print(f"x1=x2={x1}")
    else:
        d = format(math.sqrt(-delta) / (2 * a), ".5f")
        re = format((-b) / (2 * a), ".5f")
        print(f"x1={re}+{d}i;x2={re}-{d}i")'''