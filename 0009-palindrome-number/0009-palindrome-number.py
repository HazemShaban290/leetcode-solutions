class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:return False
        num=x
        reverse=0
        while num!=0:
            reverse=10*reverse+num%10
            num/=10
        return reverse==x

