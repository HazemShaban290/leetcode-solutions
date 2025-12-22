class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n<=2:
            return n
        memo=[None for _ in range(n+1) ]
        memo[0],memo[1],memo[2]=1,1,2
        def countPossibilities(numOfNodes):
            if memo[numOfNodes] is not None:
                return memo[numOfNodes]
            uniqueSubTree=0
            for i in range(1,numOfNodes+1):
                print(numOfNodes,numOfNodes-i , i-1)
                uniqueSubTree+=countPossibilities(numOfNodes-i)*countPossibilities(i-1)
            memo[numOfNodes]=uniqueSubTree
            return uniqueSubTree
        countPossibilities(n)
        return memo[n]