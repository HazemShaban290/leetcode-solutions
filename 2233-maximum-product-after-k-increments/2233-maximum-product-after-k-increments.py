import heapq
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        
        for _ in range(k):
            smallest=heapq.heappop(nums)
            smallest+=1
            heapq.heappush(nums,smallest)
        product=1
        for num in nums:
            product=(product * num) % ((10**9)+7)
        return product % ((10**9)+7)