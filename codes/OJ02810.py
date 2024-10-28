from math import pow, isclose
def main():
	cube = []
	n = int(input())
	for b in range(2, n-2):
		for c in range(b, n-1):
			for d in range(c, n):
				a = pow(pow(b, 3) + pow(c, 3) + pow(d, 3), 1/3)
				if isclose(a, int(a+0.5), abs_tol = 1e-9) and int(a+0.5) <= n:
					cube.append([int(a+0.5), b, c, d])
	cube.sort(key = lambda t: (t[0], t[1], t[2], t[3]))
	for c in cube:
		print(f"Cube = {c[0]}, Triple = ({c[1]},{c[2]},{c[3]})")
if __name__ == '__main__':
	main()