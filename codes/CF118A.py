s = list(input().lower())
for letter in s:
	if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
		continue
	print('.'+letter, end = '')