class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashMap={0:-1}
        currSum=0
        for i in range(len(nums)):
            currSum+=nums[i]
            remainder = currSum % k 
            if remainder in hashMap:
                if i-hashMap[remainder]>=2:
                    return True
            else:
                hashMap[remainder]=i
        return False