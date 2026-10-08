class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        count=1
        for i in range(1,len(s)):
            el=s[i]
            if el=='(':
                if count>0:
                    res.append(el)
                count+=1
            else:
                count-=1
                if count>0:
                    res.append(el)
        return "".join(res)

