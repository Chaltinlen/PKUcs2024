'''打个表？'''
# prime = [True for i in range(int(1e3))]
# prime[0] = False
# prime[1] = False
# for i in range(2, int(1e3)):
# 	if prime[i]:
# 		j = 2
# 		while j * i < 1e3:
# 			prime[j * i] = False
# 			j += 1
# for i in range(int(1000)):
# 	if prime[i]:
# 		print(i, end = ",") 

# 1-1000 的质数
# prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,431,433,439,443,449,457,461,463,467,479,487,491,499,503,509,521,523,541,547,557,563,569,571,577,587,593,599,601,607,613,617,619,631,641,643,647,653,659,661,673,677,683,691,701,709,719,727,733,739,743,751,757,761,769,773,787,797,809,811,821,823,827,829,839,853,857,859,863,877,881,883,887,907,911,919,929,937,941,947,953,967,971,977,983,991,997,1009]

# from math import isqrt, pow
# def isprime(n):
# 	s = isqrt(n) + 1
# 	if n == 1:
# 		return False

# 	for i in prime:
# 		if i >= s:
# 			return True
# 		if n % i == 0:
# 			return False


# n = int(input())
# num = list(map(int, input().split()))
# for p in num:
# 	isqp = isqrt(p)
# 	if pow(isqp, 2) != p:
# 		print("NO")
# 		continue
# 	if isprime(isqp):
# 		print("YES")
# 		continue
# 	print("NO")

from math import isqrt, pow
def main():
	primes = []
	append = primes.append
	
	primesstatus = [True for i in range(int(1e6 + 1))]
	primesstatus[0], primesstatus[1] = False, False
	for i in range(2, int(1e6 + 1)):
		if primesstatus[i]:
			append(i)
		for j in primes:
			if i * j > 1e6:
				break
			primesstatus[i * j] = False
			if i % j == 0 and j != i:
				break
			
	for i in range(len(primes)):
		primes[i] *= primes[i]
	
	n = int(input())
	num = list(map(int, input().split()))
	for i in num:
		isqrp = isqrt(i)
		if pow(isqrp, 2) != i:
			print("NO")
			continue
		# up, down = 78497, 0
		# while True:
		# 	if up < down:
		# 		print("NO")
		# 		break
		# 	mean = (up+down)>>1
		# 	if i == primes[mean]:
		# 		print("YES")
		# 		break
		# 	elif i < primes[mean]:
		# 		up = mean - 1
		# 	else:
		# 		down = mean + 1
		if primesstatus[isqrp]:
			print("YES")
		else:
			print("NO")

main()