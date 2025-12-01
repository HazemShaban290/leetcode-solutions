class Solution(object):
    def wordBreak(self, s, wordDict,start=0):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        visited=set()
        return self.dfs(s,wordDict,0,visited)
        
    def dfs(self,s,wordDict,start,visited):
        for i in range(start,len(s)):
            if s[start:i+1] in wordDict:
                if i+1 == len(s):
                    return True
                if i+1 not in visited:
                    
                    if self.dfs(s, wordDict,i+1,visited):
                        return True
                    else:
                        visited.add(i+1)
        return False
                        
            