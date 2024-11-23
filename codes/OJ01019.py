from bisect import bisect_left
seq = ""
length = 0
length_sum = 0
sums = []
append = sums.append
for i in range(1, 33000):
	seq += str(i)
	length += len(str(i))
	length_sum += length
	append(length_sum)
for t in range(int(input())):
	if (x := int(input())) == 1:
		print(1)
	else:
		print(seq[x-sums[bisect_left(sums, x)-1]-1])