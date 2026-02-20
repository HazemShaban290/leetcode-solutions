class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodNumbers=set()
        bad={3,7,4}
        good={2,5,6,9}
        for i in range(1,n+1):
            valid=False
            x=i
            while x !=0:
                if x in goodNumbers:
                    valid=True
                    break
                digit =x%10
                x=x//10
                if digit in good:
                    valid=True
                elif  digit in bad:
                    valid=False
                    break
            if valid :
                goodNumbers.add(i)
        return len(goodNumbers)

                