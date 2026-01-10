class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        dp=[1 for _ in nums]
        prev=[-1 for _ in nums]
        nums.sort()
        maxSubSetInfo=[-1,float('-inf')]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    if dp[i]<dp[j]+1:
                        prev[i]=j
                        dp[i]=dp[j]+1
                if dp[i]>maxSubSetInfo[1]:
                    maxSubSetInfo[0]=i
                    maxSubSetInfo[1]=dp[i]
            
        res=[]
        index=maxSubSetInfo[0]
        for i in range(maxSubSetInfo[1]):
            res.append(nums[index])
            index=prev[index]
        return res
            