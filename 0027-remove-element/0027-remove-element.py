class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        removedNumber=0
        for i in range(len(nums)):
            if nums[i]==val:
            
                j=i
                while j<len(nums) and nums[j]==val:
                    j+=1
                if j==len(nums):
                    break
                nums[i],nums[j]=nums[j],nums[i]
        for n in nums:
           if n!=val: 
                removedNumber+=1

        return removedNumber
        