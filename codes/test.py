from random import randint
n = randint(1, 100)
times = 0
while True:
	times += 1
	guess = int(input())
	if guess > n:
		print("Too big!")
	elif guess < n:
		print("Too small!")
	else:
		print("Yes!")
		break
print(f"You have worked out the number with {times} guess(es)")