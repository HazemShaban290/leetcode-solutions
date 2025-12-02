class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        numOfDigits=self.nummberOfDigits(x)
        newNumber=0
        y=x
        while y!=0:
            print(y,numOfDigits)
            newNumber+=(y%10) * 10**(numOfDigits-1)
            numOfDigits-=1
            y=y/10
        return newNumber==x
    
    def nummberOfDigits(self,n):
        numOfDigits=0
        while n !=0:
            n=n/10
            numOfDigits+=1
        return numOfDigits