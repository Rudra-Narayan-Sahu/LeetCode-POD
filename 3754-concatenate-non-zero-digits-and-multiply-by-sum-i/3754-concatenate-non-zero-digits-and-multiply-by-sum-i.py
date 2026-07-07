class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s=0
        x=0
        for ch in str(n):
            if int(ch)!=0:
                s+=int(ch)
                x=x*10+int(ch)
        return x*s
        