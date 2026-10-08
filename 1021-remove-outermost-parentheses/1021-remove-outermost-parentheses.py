class Solution(object):
    def removeOuterParentheses(self, s):
        count=0
        ans=""
        for i in s:
            if i=='(':
                count+=1
                if count>1:
                    ans+=i
            else:
                count-=1
                if count>0:
                    ans+=i
        return ans