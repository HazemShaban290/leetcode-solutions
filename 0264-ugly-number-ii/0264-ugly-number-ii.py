import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        minHeap=[]
        heapq.heappush(minHeap,1)
        seenNumbers=set([1])
        primes=[2,3,5]
        for _ in range(n):
            currentUgly=heapq.heappop(minHeap)
            for prime in primes:
                nextUgly=prime*currentUgly
                if nextUgly not in seenNumbers:
                    heapq.heappush(minHeap,nextUgly)
                    seenNumbers.add(nextUgly)
        return currentUgly