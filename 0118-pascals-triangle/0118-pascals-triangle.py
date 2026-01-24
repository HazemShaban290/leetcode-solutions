class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle=[]
        for i in range(numRows):
            triangle.append([])
            for j in range(i+1):
                triangle[i].append(1)
                if i>=2 and j>0 and j<i:
                    triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
                
        return triangle