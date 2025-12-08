class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        visited={}
        def numberOfWays(s,i):
        
            if i ==len(s):
                return 1
            if s[i]=='0':return 0
            if i not in visited:
                visited[i]=(numberOfWays(s,i+1) if int(s[i:i+1])>0 and  int(s[i:i+1])<27 else 0) + (numberOfWays(s,i+2) if i+2<=len(s) and int(s[i:i+2])>0 and  int(s[i:i+2])<27 else 0)
            return visited[i]
        return numberOfWays(s,0)