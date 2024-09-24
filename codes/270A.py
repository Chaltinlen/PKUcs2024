'''
angle = []
for i in range(1, 180):
	if 360 % i == 0:
		angle.append(180 - i)
print(angle)
'''
angle = [179, 178, 177, 176, 175, 174, 172, 171, 170, 168, 165, 162, 160, 156, 150, 144, 140, 135, 120, 108, 90, 60]
t = int(input())
for i in range(t):
	if int(input()) in angle:
		print("YES")
	else:
		print("NO")