class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        reversedNumber=0
        neg=False
        if x<0:
            neg=True
            x*=-1
        while x !=0:
            digit=x%10
            reversedNumber=reversedNumber*10 + digit
            x/=10
        if neg:
            reversedNumber*=-1
        
        return reversedNumber if reversedNumber<2**31 and reversedNumber>=-1*(2**31) else 0