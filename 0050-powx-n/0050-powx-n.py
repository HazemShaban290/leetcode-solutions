class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            n*=-1
            x=1/x
        memo={0:1,1:x}
        def myPowHelper(x,n):
            if n in memo:
                return memo[n]
            mid=n//2
            memo[n]=myPowHelper(x,mid) *myPowHelper(x,n-mid)
            return memo[n]
        return myPowHelper(x,n)