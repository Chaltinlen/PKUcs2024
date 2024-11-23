def Hannoi(n, stt, wth, end):
	if n == 1:
		print(f"{stt}->{end}")
	else:
		Hannoi(n-1, stt, end, wth)
		print(f"{stt}->{end}")
		Hannoi(n-1, wth, stt, end)
def main():
	n = int(input())
	print(2**n - 1)
	Hannoi(n, "A", "B", "C")
main()