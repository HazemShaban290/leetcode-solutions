from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting =defaultdict(list)
        for word in words:
           waiting[word[0]].append(word)
        count=0
        for ch in s:
            if ch in waiting:
                waitingList=waiting[ch]
                waiting[ch]=[]
                for word in waitingList:
                    if len(word)==1:
                        count+=1
                    else:
                        waiting[word[1]].append(word[1:])
        return count

