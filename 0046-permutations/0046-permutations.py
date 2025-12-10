class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation=[]
        results=[]
        used=[False for _ in nums]
        def getAllPermutation():
            
            if len(nums) ==len(permutation):
                results.append(permutation[:])
                return 
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                permutation.append(nums[i])
                getAllPermutation()
                used[i]=False
                permutation.pop()
        getAllPermutation()
        return results