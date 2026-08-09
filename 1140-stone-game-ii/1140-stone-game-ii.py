
class Solution(object):
    def stoneGameII(self, piles):
        n=len(piles)
        self.dp={}
        return self.solveAlice(piles,1,0,1)
    #@lru_cache(None)
    def solveAlice(self,piles,person,i,m):
        if i>=len(piles):
            return 0
        res=-1 if person==1 else float('inf')
        key=(person,i,m)
        if key in self.dp:
            return self.dp[key]
        stone=0
        for x in range(1,min(2*m,len(piles)-i)+1):
            stone+=piles[i+x-1]
            if person==1:
                res=max(res,stone+self.solveAlice(piles,0,i+x,max(x,m)))
            else:
                res=min(res,self.solveAlice(piles,1,i+x,max(x,m)))
        self.dp[key]=res
        return res