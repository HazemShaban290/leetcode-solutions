class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def compress(string):
            compressed=[]
            count=0
            char=string[0]
            for i in range(len(string)):
                if char == string[i]:
                    count+=1
                else:
                    compressed.append(str(count)+char)
                    count=1
                    char=string[i]
            compressed.append(str(count)+char)
            return ''.join(compressed)
        def countAndSay(n):
            if n==1:return '1'
            return compress(countAndSay(n-1))
        return countAndSay(n)