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
            for charCount in range(1,4):
                if i+charCount <=len(s) and int(s[i:i+charCount]) <=255:
                    if charCount>1 and s[i]=='0': continue
                    ip.append(s[i:i+charCount])
                    getIPAddresses(s,dots-1,i+charCount)
                    ip.pop()

        getIPAddresses(s,3,0)
        return IPs

        