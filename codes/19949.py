n = int(input())
sum = 0
string = []
for i in range(0, n):
	string.append(input())
	sum += (string[i].count("###") - 2 * string[i].count("### ###"))

print(str(int(sum / 2)))