s = input()
index = 0
for letter in "hello":
	index = s.find(letter)
	if index == -1:
		print("NO")
		exit()
	s = ''.join(list(s)[index + 1:])
print("YES")