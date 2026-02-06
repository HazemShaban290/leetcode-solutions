class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        allCap=True
        allSmall=True
        firstCap=True
        for i in range(len(word)):
            if word[i] >="A" and word[i]<="Z":
                if i>0:
                    firstCap=False
                allSmall=False
            else:
                allCap=False
        return allCap or allSmall or firstCap
            
            