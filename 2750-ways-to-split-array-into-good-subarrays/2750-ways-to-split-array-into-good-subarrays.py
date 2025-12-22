class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        zeroCount=0
        ways=1
        firstOneFound=False
        for i in range(len(nums)):
            if nums[i]==1:
                if zeroCount!=0:
                    ways=(ways*(zeroCount+1))%((10**9)+7)
                zeroCount=0
                firstOneFound=True
            else:
                if firstOneFound:
                    zeroCount+=1
        if not firstOneFound:
            return 0
        return ways %((10**9)+7)