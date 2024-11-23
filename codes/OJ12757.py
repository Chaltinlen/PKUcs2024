def main():
	num = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
	neg = 0
	integer = input().split()
	ans = 0
	buffer = 0
	if integer[0] == 'negative':
		neg = -1
		stt = 1
	else:
		stt = 0
		neg = 1
	for i in range(stt, len(integer)):
		if integer[i] == "hundred":
			buffer = buffer - num[integer[i-1]] + num[integer[i-1]] * 100
		elif integer[i] == "thousand":
			buffer *= 1000
		elif integer[i] == "million":
			ans += buffer * 1000000
			buffer = 0
		else:
			buffer += num[integer[i]]
	print(neg * (ans+buffer))

main()