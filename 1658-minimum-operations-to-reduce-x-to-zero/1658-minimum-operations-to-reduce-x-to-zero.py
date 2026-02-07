class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        targetSumSub=sum(nums)-x
        if targetSumSub==0:
            return len(nums)
        minOperations=float('inf')
        hashMap={0:-1}
        currSum= 0
        for i in range(len(nums)):
            currSum+=nums[i]
            if currSum-targetSumSub in hashMap:
                operations=len(nums)-(i-hashMap[currSum-targetSumSub])
                minOperations=min(minOperations,operations)
            hashMap[currSum]=i
        return minOperations if minOperations!=float('inf') else -1

