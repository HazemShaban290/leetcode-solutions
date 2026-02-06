class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a!=b:
            return len(a) if len(a)>len(b) else len(b)
        else:
            return -1