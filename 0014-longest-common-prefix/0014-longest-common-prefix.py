class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs[0]=="":
            return ""
        lcp=strs[0]
        for string in strs:
            i=0
            while i <len(lcp) and i<len(string) and string[i]==lcp[i]:
                i+=1
            lcp=string[0:i]
            if lcp=="":break
        return lcp