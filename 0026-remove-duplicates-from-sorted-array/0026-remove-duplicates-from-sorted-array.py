class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueNumbers=1
        currNum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=currNum:
                nums[uniqueNumbers]=nums[i]
                currNum=nums[i]
                uniqueNumbers+=1
        return uniqueNumbers