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