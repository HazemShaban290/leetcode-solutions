class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxCurrSum=0
        maxSoFar=0
        for num in nums:
            maxCurrSum=max(maxCurrSum+num,0)
            maxSoFar=max(maxSoFar,maxCurrSum)
        if maxSoFar==0:
            return max(nums)
        return maxSoFar