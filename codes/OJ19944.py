week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
n = int(input())
w = []
for i in range(n):
	date = list(input())
	c = int(''.join(date[0:2]))
	y = int(''.join(date[2:4]))
	m = int(''.join(date[4:6]))
	d = int(''.join(date[6:]))
	if m == 2 or m == 1:
		m += 12
		if y == 0:
			c -= 1
			y = 99
		else:
			y -= 1
	w.append(week[(y + y//4 + c//4 - 2*c + 26*(m + 1)//10 +d-1) % 7])

for day in w:
	print(day)


