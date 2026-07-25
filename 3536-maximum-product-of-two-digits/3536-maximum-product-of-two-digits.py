class Solution(object):
    def maxProduct(self, n):
        s=str(n)
        num=[]
        for ch in s:
            num.append(int(ch))
        print(num)
        num.sort()
        return num[len(num)-1]*num[len(num)-2]