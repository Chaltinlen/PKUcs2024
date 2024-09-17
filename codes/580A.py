n = int(input())
a = list(map(int, input().split()))
max_nondecreasing = [1 for j in range(n)]
index = 0
i = 1
while i < n:
	while a[i] >= a[i-1]:
		max_nondecreasing[index] += 1
		if i < n - 1:
			i += 1
		else:
			break
#		print("i: "+ str(i))
	i += 1
	index += 1

#print(str(index))
#print(max_nondecreasing)
print(str(int(max(max_nondecreasing))))