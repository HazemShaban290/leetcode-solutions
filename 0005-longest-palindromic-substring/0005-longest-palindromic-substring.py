class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest=[0,1]
        for i in range(1,len(s)):
            if i<len(s)-1 and s[i+1]==s[i-1]:
                self.findLongest(i-1,i+1,s,longest)
            if s[i]==s[i-1]:
                self.findLongest(i-1,i,s,longest)
            
        return s[longest[0]:longest[1]]
    def findLongest(self,left,right,s,longest):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1 
            right+=1
        left+=1
        right-=1
        if right+1 - left > longest[1]-longest[0]:
            longest[0]=left
            longest[1]=right+1