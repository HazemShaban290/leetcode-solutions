class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequences=set([s[0:10]])
        repSequences=set()
        for i in range(10,len(s)):
            seq=s[i-9:i+1]
            if seq in sequences:
               repSequences.add(seq)
            sequences.add(seq)
        return  list(repSequences)
            


