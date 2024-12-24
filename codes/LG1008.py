# from itertools import permutations, batched
# from functools import partial
# li = map(partial(batched, n=3), permutations(range(1, 10)))
# for num in li:
#     num = list(num)
#     for i in range(3):
#         num[i] = num[i][0] * 100 + num[i][1] * 10 + num[i][2]
#     if 6 * num[0] == 3 * num[1] == 2 * num[2]:
#         print(*num, sep=" ")
print("""192 384 576
219 438 657
273 546 819
327 654 981""")
# batched()居然在Python3.12才加入，不能理解
