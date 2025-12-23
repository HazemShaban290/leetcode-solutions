class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        visited={}
        def traverse(i,j,k):
            if (i,j,k) in visited:return visited[(i,j,k)]
            if k==len(s3) and (i !=len(s1) or j!=len(s2)):
                return False
            elif k==len(s3) and i ==len(s1) and j==len(s2):
                return True
            option1=False
            option2=False
            if j<len(s2) and s2[j]==s3[k]:
                option1=traverse(i,j+1,k+1)
            if i<len(s1) and s1[i]==s3[k]:
                option2=traverse(i+1,j,k+1)
            visited[(i,j,k)]=option1 or option2 
            return visited[(i,j,k)]
        return traverse(0,0,0)