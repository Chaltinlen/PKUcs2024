# 中国剩余定理
# def exgcd(a, b):
# 	if b == 0:
# 		x = 1
# 		y = 0
# 		return x, y
# 	x1, y1 = exgcd(b, a%b)
# 	x = y1
# 	y = x1 - a//b*y1
# 	return x, y

def main():
	for cnt in range(1, int(1e9)):
		p, e, i, d = map(int, input().split())
		if i == -1:
			break
		x = (1288*i - 6831*e+ 5544*p) % 21252 - d
		print(f"Case {cnt}: the next triple peak occurs in {(x-1) % 21252 + 1} days.")

if __name__ == '__main__':
	main()