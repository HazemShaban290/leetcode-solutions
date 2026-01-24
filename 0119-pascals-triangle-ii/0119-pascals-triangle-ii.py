class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle=[]
        for i in range(rowIndex+1):
            triangle.append([])
            for j in range(i+1):
                triangle[i].append(1)
                if i>=2 and j>0 and j<i:
                    triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
                
        return triangle[-1]