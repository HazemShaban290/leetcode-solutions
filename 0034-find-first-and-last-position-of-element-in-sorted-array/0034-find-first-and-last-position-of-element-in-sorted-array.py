class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
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
                i,j=middle,middle
                while i>=0 and nums[i]==target :
                    i-=1
                while  j<len(nums) and nums[j]==target:                
                    j+=1
                return [i+1,j-1]
        return [-1,-1]
                