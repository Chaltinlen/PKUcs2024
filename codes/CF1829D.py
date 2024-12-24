from math import gcd, log2, log, pow
pow2 = {128, 1, 2, 256, 4, 512, 1024, 2048, 8, 4096, 32768, 131072, 262144, 524288, 8192, 1048576, 16, 16384, 4194304, 32, 8388608, 64, 65536, 2097152}
pow3 = {1, 6561, 3, 19683, 177147, 9, 59049, 2187, 81, 531441, 243, 1594323, 729, 27, 4782969}

for i in range(int(input())):
    n, m = map(int, input().split())
    if n < m:
        print("NO")
        continue
    if n == m:
        print("YES")
        continue
    gcmn = gcd(m, n)
    m = (m // gcmn)
    n = (n // gcmn)
    if n not in pow3:
        print("NO")
        continue
    print("NO" if m not in pow2 or log2(m) > log(n, 3) else "YES")