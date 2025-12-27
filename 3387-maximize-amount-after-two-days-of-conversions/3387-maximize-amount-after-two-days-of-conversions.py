class Solution(object):
    def maxAmount(self, initialCurrency, pairs1, rates1, pairs2, rates2):
        """
        :type initialCurrency: str
        :type pairs1: List[List[str]]
        :type rates1: List[float]
        :type pairs2: List[List[str]]
        :type rates2: List[float]
        :rtype: float
        """
        
        def constructGraph(pairs,rates):
            graph={}
            for pair ,rate in zip(pairs, rates):
                if pair[0] not in graph:
                    graph[pair[0]]={}
                if pair[1] not in graph:
                    graph[pair[1]]={}
                graph[pair[0]][pair[1]]=rate
                graph[pair[1]][pair[0]]=1/rate
                
            return graph
        graph1=constructGraph(pairs1,rates1)
        graph2=constructGraph(pairs2,rates2)
        def getMaxProductConvetions(graph, startingNode):
            maxProduct={}
            for node in graph.keys():
                maxProduct[node]=float('-inf')
            maxProduct[startingNode]=1
            for _ in range(len(graph)-1):
                for node in graph:
                    if maxProduct[node] == float('-inf'):continue
                    for destination in  graph[node]:
                        maxProduct[destination]=max(maxProduct[destination],maxProduct[node]*graph[node][destination])
            return maxProduct
        maxProduct1=getMaxProductConvetions(graph1,initialCurrency)
        ultimateMaxProduct=float('-inf')
        if initialCurrency not in graph2:
            return maxProduct1[initialCurrency]
        for currency in  maxProduct1:
            maxProduct2=getMaxProductConvetions(graph2,currency)
            ultimateMaxProduct=max(ultimateMaxProduct,maxProduct2[initialCurrency]*maxProduct1[currency])
        return ultimateMaxProduct