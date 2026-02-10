class Solution:
    def checkIsSubSeq(self,word1,word2):
        p1 ,p2=0,0
        while p1<len(word1) and p2<len(word2):
            if word1[p1]==word2[p2]:
                p1+=1
                p2+=1
            else:
                p1+=1
        return p2==len(word2)
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        counter={}
        for word in words:
            counter[word]=counter.get(word,0)+1
        
        count=0
        for word in counter.keys():
            if self.checkIsSubSeq(s,word):
                count+=counter[word]
        return count