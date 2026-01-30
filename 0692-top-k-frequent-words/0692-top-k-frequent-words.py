import heapq
from typing import List

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = {}

        for word in words:
            counter[word] = counter.get(word, 0) + 1

        heap = []

        for word, count in counter.items():
            heapq.heappush(heap, (-count, word))

        result = []
        for _ in range(k):
            count, word = heapq.heappop(heap)
            result.append(word)

        return result