class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[0])
        i=0
        removed=0
        while i<len(intervals) :
            j=i+1
            while j<len(intervals) and intervals[j][0]<intervals[i][1]:
                removed+=1
                if intervals[j][1] >=intervals[i][1]:
                    j+=1
                else:
                    break

            i=j
        return  removed
        
        
