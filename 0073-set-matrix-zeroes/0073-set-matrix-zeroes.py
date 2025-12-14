class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        zerosAtfirstCol=False
        rows=len(matrix)
        cols=len(matrix[0])
        for i in range(cols):
            if matrix[0][i]==0:
              zerosAtfirstCol=True
              break
        zerosAtfirstRow=False
        for i in range(rows):
            if matrix[i][0]==0:
              zerosAtfirstRow=True
              break
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
        for i in range(1,rows):
            for j in range(1,cols):
                if matrix[0][j]==0 or matrix[i][0]==0:
                    matrix[i][j]=0
        if zerosAtfirstRow:
            for i in range(rows):
                matrix[i][0]=0
                    
        if zerosAtfirstCol:
            for i in range(cols):
                matrix[0][i]=0         