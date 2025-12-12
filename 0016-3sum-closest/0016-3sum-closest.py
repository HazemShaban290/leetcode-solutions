class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestSum=float('inf')
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                currSum=nums[i]+nums[left]+nums[right]
                if currSum>target:
                    right-=1
                elif currSum<target:
                    left+=1
                else:
                    return currSum
                if abs(currSum-target)<abs(closestSum-target):
                    closestSum=currSum
        return closestSum