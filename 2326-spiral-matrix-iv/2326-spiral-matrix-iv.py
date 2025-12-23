# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def spiralMatrix(self, m, n, head):
        """
        :type m: int
        :type n: int
        :type head: Optional[ListNode]
        :rtype: List[List[int]]
        """
        output=[[-1 for _ in range(n)] for _ in range(m)]
        node =head
        startRow=0
        startCol=0
        endRow=m-1
        endCol=n-1
        while node :
            for col in range(startCol,endCol+1):
                output[startRow][col]=node.val
                node=node.next 
                if not node: return output
            for row in range(startRow+1,endRow+1):
                output[row][endCol]=node.val
                node=node.next 
                if not node: return output
            for col in range(endCol-1,startCol-1,-1):
                output[endRow][col]=node.val
                node=node.next 
                if not node: return output
            for row in range(endRow-1,startRow,-1):
                output[row][startCol]=node.val
                node=node.next 
                if not node: return output
            endCol-=1
            startCol+=1
            startRow+=1
            endRow-=1
        return output
            