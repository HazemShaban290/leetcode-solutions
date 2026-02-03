# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.rowLargestValue=[]
        def getLargestValuesInEachRow(node,level):
            if not node:return
            if level==len(self.rowLargestValue):
                self.rowLargestValue.append(node.val)
            else:
                self.rowLargestValue[level]=max(self.rowLargestValue[level],node.val)
            getLargestValuesInEachRow(node.left,level+1)
            getLargestValuesInEachRow(node.right,level+1)
        getLargestValuesInEachRow(root,0)
        return self.rowLargestValue