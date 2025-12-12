class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueNumbers=0
        currNum=nums[0]-1
        for i in range(0,len(nums)):
            if nums[i]!=currNum:
                nums[uniqueNumbers]=nums[i]
                currNum=nums[i]
                uniqueNumbers+=1
        return uniqueNumbers