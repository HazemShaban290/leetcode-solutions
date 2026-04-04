class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minVal=arrays[0][0]
        maxVal=arrays[0][-1]
        minDis=0
        for i in range(1,len(arrays)):
            minDis=max(minDis,abs(arrays[i][0]-minVal),abs(arrays[i][-1]-maxVal))
            minVal=min(arrays[i][0])
            maxVal=max(arrays[i][-1])
        return minDis