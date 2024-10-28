n = int(input())
boy = sorted(list(map(int, input().split())))
m = int(input())
girl = sorted(list(map(int, input().split())))
cnt = 0
i, j = 0, 0
while i < n:
	while j < m:
		if abs(boy[i] - girl[j]) < 2:
			cnt += 1
			j += 1
			break
		if girl[j] > boy[i]:
			break
		else:
			j += 1
	i += 1
print(cnt)