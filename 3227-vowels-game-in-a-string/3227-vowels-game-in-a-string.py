class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels=['a','e','o','u','i']
        countVowels=0
        for char in s:
            if char in vowels:
                countVowels+=1
        return countVowels!=0