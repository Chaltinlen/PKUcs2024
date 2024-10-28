keyboard = list("qwertyuiopasdfghjkl;zxcvbnm,./")
pos = 0
if input() == 'L':
	pos = 1
else:
	pos = -1
sentence = list(input())
for i in range(len(sentence)):
	sentence[i] = keyboard[keyboard.index(sentence[i]) + pos]
print(''.join(sentence))