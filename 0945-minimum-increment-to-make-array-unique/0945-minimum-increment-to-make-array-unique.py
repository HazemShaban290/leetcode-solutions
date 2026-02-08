class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        nextFree=0
        moves=0
        for num in nums:
            if num<nextFree:
                moves+=nextFree-num
            else:
                nextFree=num
            nextFree+=1
        return moves