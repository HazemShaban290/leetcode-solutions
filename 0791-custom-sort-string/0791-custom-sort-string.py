class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter={}
        for char in s:
            counter[char]=counter.get(char,0)+1
        res=[]
        for char in order:
            if char in counter:
                for _ in range(counter[char]):
                    res.append(char)
                    counter[char]-=1
        for char in counter.keys():
            if counter[char]!=0:
                for _ in range(counter[char]):
                    res.append(char)
        return ''.join(res)