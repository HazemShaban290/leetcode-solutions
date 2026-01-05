class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyNumbers=set([1])
        for _ in range(n):
            currentUgly=min(uglyNumbers)
            uglyNumbers.remove(currentUgly) 
            uglyNumbers.add(currentUgly*2) 
            uglyNumbers.add(currentUgly*3) 
            uglyNumbers.add(currentUgly*5)
        return currentUgly