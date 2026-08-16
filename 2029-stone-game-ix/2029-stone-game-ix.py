class Solution(object):
    def stoneGameIX(self, stones):
        n=len(stones)
        f=[0,0,0]
        for s in stones:
            f[s%3]+=1
        if f[0]%2==0:
            return min(f[1],f[2])>=1
        return abs(f[1]-f[2])>2     