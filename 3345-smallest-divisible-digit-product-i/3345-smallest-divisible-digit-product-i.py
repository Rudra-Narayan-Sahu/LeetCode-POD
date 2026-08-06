class Solution(object):
    def smallestNumber(self, n, t):
        product=1
        while True:
            s=str(n)
            if n<10:
                product*=int(s[0])
            elif n<100:
                product*=int(s[0])*int(s[1])
            else:
                product=0
            if product%t!=0:
                n+=1
                product=1
            else:
                return n
        return n
        
        