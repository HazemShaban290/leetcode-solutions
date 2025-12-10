class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        permutation=[]
        results=set()
        used=[False for _ in nums]
        def getAllPermutation():
            
            if len(nums) ==len(permutation):
                results.add(','.join(str(x) for x in permutation[:]))
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
        return [[int(x) for x in per.split(',')] for per in results]
