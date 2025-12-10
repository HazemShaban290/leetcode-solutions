class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def transpose():
            for i in range(len(matrix)):
                for j in range(i,len(matrix[0])):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        def reverseRow():
            for i in range(len(matrix)):
                start=0
                end=len(matrix[0])-1
                while start<end:
                    matrix[i][start],matrix[i][end]=matrix[i][end],matrix[i][start]
                    start+=1
                    end-=1
        transpose()
        reverseRow()
        return matrix