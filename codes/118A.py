s = list(input().lower())
#print(s)
for letter in s:
	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
		continue
	print('.'+letter, end = '')