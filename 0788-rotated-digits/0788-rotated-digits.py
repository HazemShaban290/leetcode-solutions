class Solution:
    def rotatedDigits(self, n: int) -> int:
        goodNumbers=set()
        skip={1,0,8}
        rotated={2,5,6,9}
        for i in range(1,n+1):
            changed=False
            x=i
            while x !=0:
                if x in goodNumbers:
                    changed=True
                    break
                digit =x%10
                x=x//10
                if digit in rotated:
                    changed=True
                elif  digit not in skip:
                    changed=False
                    break
            if changed :
                goodNumbers.add(i)
        return len(goodNumbers)

                