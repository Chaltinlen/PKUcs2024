while True:
	try:
		address = input()
		if address.find(".@") != -1 or address.find("@.") != -1:
			print("NO")
			continue

		address = list(address)

		if address[0] == "." or address[0] == "@" or address[-1] == "." or address[-1] == "@":
			print("NO")
			continue

		at_count = 0
		for char in address:
			if char == '@':
				at_count += 1
		if at_count != 1:
			print("NO")
			continue

		try:
			address.index(".", address.index("@"))
			print("YES")
		except:
			print("NO")
	except EOFError:
		exit()