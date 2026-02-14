import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        heap=[(-1*score[i],i) for i in range(len(score))]
        
        heapq.heapify(heap)
        place=1
        while heap:
            _,index=heapq.heappop(heap)
            if place==1:
                score[index]="Gold Medal"
            elif place==2:
                score[index]="Silver Medal"
            elif place==3:
                score[index]="Bronze Medal"
            else:
                score[index]=str(place)
            place+=1
        return score
            