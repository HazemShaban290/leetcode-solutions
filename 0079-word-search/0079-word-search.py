class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def checkExistance(i,row,col):
            if row <0 or row>=len(board) or col <0 or col>=len(board[0]) or board[row][col] !=word[i] or board[row][col]=='*' :
                return False
            if i==len(word)-1:
                return True
            char=board[row][col]
            board[row][col]='*'
            isFound= checkExistance(i+1,row+1,col) or checkExistance(i+1,row,col+1) or checkExistance(i+1,row-1,col) or checkExistance(i+1,row,col-1)
            board[row][col]=char
            return isFound

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col]== word[0]:
                    if checkExistance(0,row,col):
                        return True
        return False

        