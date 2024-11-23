h = int(input())
m = int(input())
h = 2 * h - m / 2
courses = sorted([tuple(map(float, input().split())) for i in range(m)], key = lambda c: c[0] * c[1], reverse = True)
tot = 0
for c in courses:
	maxtime = 5/c[0]
	if h > maxtime:
		h -= maxtime
		tot += 5 * c[1]
	else:
		tot += h * c[0] * c[1]
		break
print(f"{tot:.1f}")