
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter1={}
        counter2={}        
        for c in s:
            counter1[c]=counter1.get(c,0)+1
        for c in t:
            counter2[c]=counter2.get(c,0)+1
        for key in counter2:
            if key not in counter1:
                return key
            if counter1[key]<counter2[key]:
                return key
        