import math
class Solution:
    def integerReplacement(self, n: int) -> int:
        ops=0
        def dfs(n):
            if n ==1:
                return 0
            if n%2==0:
                return 1+dfs(n//2)
            else:
                return min(1+dfs(n-1),1+dfs(n+1))

        return dfs(n)

        