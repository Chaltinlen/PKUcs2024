# from itertools import groupby
# n = int(input())
# num = list(map(lambda t: sorted(t, key = lambda s: (s.ljust(6, s[0]), -len(s) if (len(s) > 1 and s[1] > s[0]) else len(s)), reverse = True), [list(group) for key, group in groupby(sorted(input().split(), key = lambda s: s[0], reverse = True), key = lambda s: s[0])]))
# print("".join(map("".join, num)), "".join(list(map("".join, reversed(list(map(reversed, num)))))))


# 两倍长度是正确的。O(nlogn)
from math import ceil
input()
lt = input().split()

max_len = len(max(lt, key=lambda x: len(x)))
print(list(map(lambda x: x * ceil(2*max_len/len(x)), lt)))
lt.sort(key=lambda x: x * ceil(2*max_len/len(x)))

lt1 = lt[::-1]
print(''.join(lt1), ''.join(lt))