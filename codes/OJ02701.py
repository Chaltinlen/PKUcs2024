# '''
# 先打表
# '''
# nonseven_squared = [0 for i in range(100)]
# sum_of_square = [0 for i in range(100)]
# for i in range(100):
# 	if i % 7 != 0 and i//10 != 7 and i % 10 != 7:
# 		nonseven_squared[i] = i**2
# print(nonseven_squared)

# # sum_of_square[0] = 1
# for i in range(1, 100):
# 	sum_of_square[i] = (nonseven_squared[i] + sum_of_square[i - 1])
# print(sum_of_square)

sum_of_square = [0, 1, 5, 14, 30, 55, 91, 91, 155, 236, 336, 457, 601, 770, 770, 995, 1251, 1251, 1575, 1936, 2336, 2336, 2820, 3349, 3925, 4550, 5226, 5226, 5226, 6067, 6967, 7928, 8952, 10041, 11197, 11197, 12493, 12493, 13937, 15458, 17058, 18739, 18739, 20588, 22524, 24549, 26665, 26665, 28969, 28969, 31469, 34070, 36774, 39583, 42499, 45524, 45524, 45524, 48888, 52369, 55969, 59690, 63534, 63534, 67630, 71855, 76211, 76211, 80835, 85596, 85596, 85596, 85596, 85596, 85596, 85596, 85596, 85596, 85596, 85596, 91996, 98557, 105281, 112170, 112170, 119395, 126791, 126791, 134535, 142456, 150556, 150556, 159020, 167669, 176505, 185530, 194746, 194746, 194746, 204547]
print(sum_of_square[int(input())])