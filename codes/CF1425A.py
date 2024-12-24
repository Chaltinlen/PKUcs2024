from sys import stdin, stdout
def take(n):
    return 1 if n % 2 or (not n % 4 and n != 4) or n == 1 else n >> 1
readin = map(int, stdin.read().split())
out = []
append = out.append
for i in range(next(readin)):
    get = 0
    n = next(readin)
    while n > 0:
        get += take(n)
        n -= take(n)
        n -= take(n)
    append(str(get))
stdout.write("\n".join(out))