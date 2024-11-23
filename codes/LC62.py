from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m+n-2, n-1)
if __name__ == '__main__':
    m, n = map(int, input().split())
    sol = Solution()
    print(sol.uniquePaths(m, n))