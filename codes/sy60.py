a, b = map(int, input().split())
have_narcissus = False
for i in range(a, b + 1):
	i1 = int(str(i)[0])
	i2 = int(str(i)[1])
	i3 = int(str(i)[2])
	if i == i1**3 + i2**3 + i3**3:
		if not have_narcissus:
			print(i, end = "")
		else:
			print(f" {i}", end = "")
		have_narcissus = True
if not have_narcissus:
	print("NO")