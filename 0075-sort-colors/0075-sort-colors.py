class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first=0
        second=0
        third=len(nums)-1
        while second <=third:
            if nums[second]==0:
                nums[first],nums[second]=nums[second],nums[first]
                first+=1
                second+=1
            elif nums[second]==2:
                nums[second],nums[third]=nums[third],nums[second]
                third-=1
            else:
                second+=1
        return nums