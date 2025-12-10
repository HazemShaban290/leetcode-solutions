class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation=[]
        results=[]
        def getAllPermutation():
            
            if len(nums) ==0:
                results.append(permutation[:])
                return 
            for i in range(len(nums)):
                permutation.append(nums[i])
                x=nums.pop(i)
                getAllPermutation()
                nums.insert(i,x)
                permutation.pop()
        getAllPermutation()
        return results