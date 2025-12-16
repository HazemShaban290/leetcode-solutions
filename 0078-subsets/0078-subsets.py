class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets=[[]]
        for num in nums:
            newSets=[]
            for sub in subsets:

                newSets.append(sub+ [num])
            subsets+=newSets
        return subsets