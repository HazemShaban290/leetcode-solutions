class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        mins=[[float('inf'),-1],[float('inf'),-1]]
        maxs=[[float('-inf'),-1],[float('-inf'),-1]]
        for i in range(len(arrays)):
            if arrays[i][0]<=mins[0][0]:
                mins[1][0]=mins[0][0]
                mins[1][1]=mins[0][1]
                mins[0][0]=arrays[i][0]
                mins[0][1]=i

            elif arrays[i][0]<=mins[1][0]:
                mins[1][0]=arrays[i][0]
                mins[1][1]=i
            if arrays[i][-1]>=maxs[0][0]:
                maxs[1][0]=maxs[0][0]
                maxs[1][1]=maxs[0][1]
                maxs[0][0]=arrays[i][-1]
                maxs[0][1]=i
            elif arrays[i][-1]>=maxs[1][0]:
                maxs[1][0]=arrays[i][-1]
                maxs[1][1]=i
        maxDis=float('-inf')
        for m in mins:
            for x in maxs:
                if m[1]!=x[1]:

                    maxDis=max(abs(x[0]-m[0]),maxDis)
        return maxDis
