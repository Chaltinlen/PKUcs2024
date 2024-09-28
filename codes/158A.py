n, k = map(int, input().split())
a = list(map(int, input().split()))
kth = a[k-1]
num = 0

for score in a:
	if score == 0 or score < kth:
		break
	num += 1

print(num)