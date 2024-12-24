from sys import stdin
pigs = [1e9]
min_pig = [1e9]
pres_min = 1e9
prompt = iter(stdin.read().split())
while (p := next(prompt, 0)):
    if p == "min" and len(pigs) != 1:
        print(min_pig[-1])
    if p == "pop" and len(pigs) != 1:
        pigs.pop()
        min_pig.pop()
        pres_min = min_pig[-1]
    if p == "push":
        pigs.append(int(next(prompt)))
        pres_min = min(pres_min, pigs[-1])
        min_pig.append(pres_min)
