from math import ceil
while True:
	n = int(input())
	if n == 0:
		exit()
	time = []
	for i in range(n):
		v, t = map(int, input().split())
		if t < 0:
			continue
		t += 4.5/v * 3600
		time.append(t)
	print(ceil(min(time)))
