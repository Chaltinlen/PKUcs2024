while True:
	try:
		a, b = list(map(int, input().split()))
		while a != 0 and b != 0:
			a %= b
			if a != 0:
				b %= a
		if a != 0:
			print(str(a))
		else:
			print(str(b))
	except EOFError:
		exit()