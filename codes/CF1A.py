m, n, a = list(map(int, input().split()))
length = m // a
width = n // a
if m % a != 0:
	length += 1
if n % a != 0:
	width += 1
print(str(length * width))