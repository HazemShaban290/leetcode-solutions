class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        romanMap={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10:'X',
            40:'XL',
            50:'L',
            90:'XC',
            100:'C',
            500:'D',
            400:'CD',
            1000:'M',
            900:'CM'
        }
        power=0
        res=''
        while num!=0:
            x=num%10
            x*=10**power
            
            if x in romanMap:
                res=romanMap[x]+res
            else:

                roman=''
                if x>(10**power)*5 :
                    roman+=romanMap[(10**power)*5]
                    x=x-(10**power)*5                
                roman+=romanMap[10**power]*(x/(10**power))
                res=roman+res
            num/=10
            power+=1
        return res
