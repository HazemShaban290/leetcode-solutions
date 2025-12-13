import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        m=len(nums1)
        n=len(nums2)
        pairs=[]
        visited=set()
        minHeap=[(nums1[0]+nums2[0],(0,0))]
        visited.add((0,0))
        while k>0:
            val,(i,j)=heapq.heappop(minHeap)
            pairs.append([nums1[i],nums2[j]])
            if i+1<m and (i+1,j) not in visited:
                visited.add((i+1,j))
                heapq.heappush(minHeap,(nums1[i+1]+nums2[j],(i+1,j)))
            if j+1<n and (i,j+1) not in visited:
                visited.add((i,j+1))
                heapq.heappush(minHeap,(nums1[i]+nums2[j+1],(i,j+1)))
            k-=1
        return pairs
                
        
       