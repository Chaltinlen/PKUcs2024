a = int(input())
if a % 2 == 1:
	print("0 0")
else:
	max_animal = a/2
	min_animal = max_animal // 2 + max_animal % 2  
	print(str(int(min_animal)) + ' ' + str(int(max_animal)))