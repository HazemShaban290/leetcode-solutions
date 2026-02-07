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
    
# prefix Sum for index i is sum from 0 -> i
# if j>i and (prefix[j] - prefix[i])%k ==0 that means the sum of numbers from i+1 to j is multiple of k
# prefix[j]%k == prefix[i]%k   then the sum of numbers from i+1 to j is multiple of k
# if the remainder appears twice that means the sum of numbers from i+1 to j is multiple of k