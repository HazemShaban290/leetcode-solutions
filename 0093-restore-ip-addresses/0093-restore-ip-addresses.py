class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        IPs=[]
        ip=[]
        def getIPAddresses(s,dots,i):
            if len(s)-i<(dots+1) or len(s)-i>(dots+1)*3:
                
                return 
            if dots ==-1 :
                IPs.append('.'.join(ip[:]))
                return
            if int(s[i:i+1]) <=255:
                ip.append(s[i:i+1])
                getIPAddresses(s,dots-1,i+1)
                ip.pop()
            if i+2 <=len(s) and int(s[i:i+2]) <=255 and s[i]!='0':
                ip.append(s[i:i+2])
                getIPAddresses(s,dots-1,i+2)
                ip.pop()
            if i+3 <=len(s) and int(s[i:i+3]) <=255 and s[i]!='0':
                ip.append(s[i:i+3])
                getIPAddresses(s,dots-1,i+3)
                ip.pop()
        getIPAddresses(s,3,0)
        return IPs

        