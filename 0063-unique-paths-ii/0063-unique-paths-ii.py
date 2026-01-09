class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows , cols=len(obstacleGrid),len(obstacleGrid[0])
        grid=[[0 for i in range(cols)] for _ in range(rows)]
        for i in range(cols):
            if obstacleGrid[0][i]==1:
                break
            grid[0][i]=1
        for i in range(rows):
            if obstacleGrid[i][0]==1:
                break
            grid[i][0]=1
        for i in range(1,rows):
            for j in range(1,cols):
                if obstacleGrid[i][j]==1:
                    continue
                 
                grid[i][j]=grid[i-1][j]+grid[i][j-1]
        return grid[-1][-1]