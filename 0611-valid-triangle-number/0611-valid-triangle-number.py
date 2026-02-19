class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        res=0
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            for j in range(i+1,n-1):
                x= nums[i]+nums[j]
                left=j+1
                right=n

                while left<right:
                    mid=(left+right)//2
                    if nums[mid]<x:
                        left=mid+1
                    elif nums[mid]>=x:
                        right=mid

                res+=left-1-j
        return res
            