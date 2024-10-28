s = int(input())
if s % 2:
	print(2 * (s-2))
if s == 4:
	print(4)
else:
	s2 = s // 2
	# 欧拉筛法打表
	primes = []
	status = [True for i in range(s)]
	status[0], status[1] = False, False
	for i in range(2, s):
		if status[i]:
			primes.append(i)
		for j in primes:
			if i * j >= s:
				break
			status[i*j] = False
			if i % j == 0 and i != j:
				break
	primesset = set(primes)
	
	if s2 % 2:
		for i in range(s2, 1, -2):
			if i in primesset and s-i in primesset:
				print(i*(s-i))
				exit()
	else:
		for i in range(s2-1, 1, -2):
			if i in primesset and s-i in primesset:
				print(i*(s-i))
				exit()
	


