import re
for i in range(int(input())):
	spreadsheet = input()
	if match := re.search(r"^([A-Z]*)(\d*)$", spreadsheet):
		col = 0
		n = len(match.group(1))
		for i in range(n):
			col += (ord(match.group(1)[i]) - 64) * pow(26, n - i - 1)
		print(f"R{match.group(2)}C{col}")
	else:
		match = re.search(r"R(\d*)C(\d*)", spreadsheet)
		col = int(match.group(2))-1
		out = []
		while col >= 0:
			out.append(chr(col % 26+65))
			col = col//26 - 1
		print(f"{''.join(out[::-1])}{match.group(1)}")