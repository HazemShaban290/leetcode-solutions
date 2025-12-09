class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        results=[]
        combination=[]
        def dfs(start , remaining):
            if remaining ==0:
                results.append(combination[:])
                return 
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if candidates[i]>remaining:
                    break
                
                combination.append(candidates[i])
                dfs(i+1,remaining-candidates[i])
                combination.pop()
        

        dfs(0,target)
        return results

    