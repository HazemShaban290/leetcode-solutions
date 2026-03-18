# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        memo={}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n ==1:
                return [TreeNode()]
            res=[] 
            for i in range(1,n,2):
                leftTrees=dfs(i)
                rightTrees=dfs(n-1-i)
                for l in leftTrees:
                    for r in rightTrees:
                        root=TreeNode()
                        root.left=l
                        root.right=r
                        res.append(root)
            memo[n]=res
            return res
        return dfs(n)