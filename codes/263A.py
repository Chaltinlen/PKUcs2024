for i in range(5):
	try:
		print(abs(i - 2)+abs(list(input().split()).index("1") - 2))
		break
	except:
		continue