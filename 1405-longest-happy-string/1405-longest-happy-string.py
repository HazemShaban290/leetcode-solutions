import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res=[]
        heap=[]
        if a>0:
            heapq.heappush(heap,(-a,'a'))
        if c>0:
            heapq.heappush(heap,(-c,'c'))
        if b>0:
            heapq.heappush(heap,(-b,'b'))
        while heap:
            count,ch= heapq.heappop(heap)
            if len(res)>=2 and ch==res[-1] and ch ==res[-2]:
                if not heap:
                    break
                count2, ch2= heapq.heappop(heap)
                res.append(ch2)
                count2+=1
                if count2<0:
                    heapq.heappush(heap,(count2,ch2))
                heapq.heappush(heap,(count,ch))
                        
            else:
                res.append(ch)
                count+=1
                if count<0:
                    heapq.heappush(heap,(count,ch))
        return ''.join(res)