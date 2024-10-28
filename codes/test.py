# from random import randint
# n = randint(1, 100)
# times = 0
# while True:
# 	times += 1
# 	guess = int(input())
# 	if guess > n:
# 		print("Too big!")
# 	elif guess < n:
# 		print("Too small!")
# 	else:
# 		print("Yes!")
# 		break
# print(f"You have worked out the number with {times} guess(es)")

# import math
# def isprime(x):
#     if x ==2:
#         return "YES"
#     elif x % 2 == 0:
#         return "NO"
#     else:
#         for i in range(1,int(math.isqrt(x))+1):
#             if x % i ==0:
#                 return "NO"
#         return "YES"



# n = int(input())
# s = list(map(int,input().split()))
# t = list(map(lambda x: int(x**0.5),s))
# results = []
# for i in t:
#     if i % 1 ==0:
#         results.append(isprime(i))
#     else:
#         results.append("NO")
# for result in results:
#     print(result)

import os
dir_path = "D:\\My_Files\\Python\\codes"
for filename in os.listdir(dir_path):
    src_file = os.path.join(dir_path, filename)
    if filename[0] == "s":
        dst_file = os.path.join(dir_path, filename.replace("sy", "SY"))
        os.rename(src_file, dst_file)