class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        currMax=nums[0]
        prevMax=0
        currMin=nums[0]
        currbits=nums[0].bit_count(        )
        for i in range(len(nums)):
            bits=nums[i].bit_count()
            if bits == currbits:
                currMin=min(currMin,nums[i])    
                currMax=max(currMax,nums[i]) 
            else:
                if currMin<prevMax:
                    return False
                prevMax=currMax
                currMin=nums[i]   
                currMax=nums[i]   
                currbits=bits
        if currMin<prevMax:
            return False
        return True
                