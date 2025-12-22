class Solution(object):
    def numberOfGoodSubarraySplits(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums)==0:
            return 0
        zeroCount=0
        ways=1
        firstOneFound=False
        for i in range(len(nums)):
            if nums[i]==1:
                if zeroCount!=0:
                    ways*=(zeroCount+1)
                zeroCount=0
                firstOneFound=True
            else:
                if firstOneFound:
                    zeroCount+=1
        return ways %((10**9)+7)