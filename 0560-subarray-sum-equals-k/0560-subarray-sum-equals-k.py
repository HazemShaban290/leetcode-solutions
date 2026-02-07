class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashMap={0:1}
        currSum=0
        appearance=0
        for num in nums:
            currSum+=num
            if currSum - k in hashMap:
                appearance+=hashMap[currSum - k]
            hashMap[currSum]=hashMap.get(currSum,0)+1
        return appearance

    
# prefix Sum for index i is sum from 0 -> i
# if j>i and (prefix[j] - prefix[i])==k that means the sum of numbers from i+1 to j is equal to k
# prefix[i] == prefix[j]-k   then the sum of numbers from i+1 to j is equal to k
# if the prefix[j]-k  appears before that means the sum of numbers from i+1 to j is equal to k