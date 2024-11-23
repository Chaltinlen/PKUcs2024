from sys import stdin, stdout
def main():
	get = list(map(int, stdin.read().split()))
	n = get[0]
	q = get[1]
	status = [[False for i in range(n)] for j in range(n)]
	for i in range(2, 2*q+1, 2):
		status[get[i]-1][get[i+1]-1] = True
	for i in range(2, 2*q+1, 2):
		if status[get[i+1]-1][get[i]-1]:
			stdout.write("Yes\n")
			break
	else:
		stdout.write("No\n")

if __name__ == '__main__':
	main()