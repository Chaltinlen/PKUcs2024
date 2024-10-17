from collections import Counter
from math import ceil
n = int(input())
friends = Counter(map(int, input().split()))
print(friends[4] + friends[3] + ceil(friends[2]/2) + max(0, ceil((friends[1] - friends[3] - 2*(friends[2] % 2))/4)))