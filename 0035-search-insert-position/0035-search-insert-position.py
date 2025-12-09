class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start =0 
        end=len(nums)-1
        while start<=end:
            middle =(start+end)//2
            if nums[middle]>target:
                end = middle-1
            elif nums[middle]<target:
                start=middle+1
            else:
               return middle
        return middle +1 if target>nums[middle] else middle