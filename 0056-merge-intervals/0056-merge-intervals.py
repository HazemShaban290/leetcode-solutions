import heapq
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        intervals.sort(key=lambda x:x[0])
        mergedIntervals=[]
        currInterval= intervals[0]
        for i in range(1,len(intervals)):
            interval= intervals[i]
            if interval[0]>currInterval[1]:
                mergedIntervals.append(currInterval[:])
                currInterval=interval
            else:
                currInterval[1]=max(currInterval[1],interval[1])
        mergedIntervals.append(currInterval[:])
        return mergedIntervals
