n = int(input())
a = list(map(int, input().split()))
K = int(input())
num_set = 0
for i in a:
	if K - i in a[a.index(i) + 1:]:
		num_set += 1
print(num_set)