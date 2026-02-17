class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        def isSubString(word1,word2):
            for i in range(len(word1)-len(word2)+1):
                if word1[i]==word2[0]:
                    if word1[i:i+len(word2)]==word2:
                        return True
            return False
        
        res=set()
        for word in words:
            for word2 in words:
                if word!=word2 and word in word2:
                    
                    res.add(word)
        return list(res)
        