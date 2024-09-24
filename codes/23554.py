n = int(input())
in_class = []
not_in_class = []
other_class = []
in_queue = list(map(int, input().split()))
for i in in_queue:
	if i > n:
		other_class.append(i)
	else:
		in_class.append(i)

for i in range(1, n+1):
	if i not in in_class:
		not_in_class.append(i)

print(" ".join(map(str, not_in_class)))
print(" ".join(map(str, sorted(other_class))))
# isfirst = False

# for i in range(1, n+1):
# 	if i not in in_class:
# 		if not isfirst:
# 			print(f"{i}", end = "")
# 		else:
# 			print(f" {i}", end = "")
# 		isfirst = True

# print()

# for i in range(len(other_class)):
# 	# if i != len(other_class) - 1:
# 		print(other_class[i], end = " ")
# 	# else:
# 	# 	print(other_class[i])
