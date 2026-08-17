class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def checkPalindrom(string):
            return string==string[::-1]
        def backtrack(start,subStrings):
            if start==len(s):
                result.append(subStrings.copy())
                return
            for end in range(start,len(s)):
                if checkPalindrom(s[start:end+1]):
                    subStrings.append(s[start:end+1])
                    backtrack(end+1,subStrings)
                    subStrings.pop()
        backtrack(0,[])
        return result