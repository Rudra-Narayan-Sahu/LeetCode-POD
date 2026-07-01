class Solution(object):
    def calculate(self, s):
        stack=[]
        number=0
        sign=1
        res=0
        for ch in s:
            if ch.isdigit():
                number=number*10+int(ch)
            elif ch=='+':
                res+=sign*number
                number=0
                sign=1
            elif ch=='-':
                res += sign * number
                number = 0
                sign = -1
            elif ch=='(':
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1
            elif ch==')':
                res+=sign*number
                number=0
                res*=stack.pop()   # sign before '('
                res+=stack.pop()
        res+=sign*number
        return res
        