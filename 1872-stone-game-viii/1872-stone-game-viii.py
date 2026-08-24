class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n=len(stones)
        # pre=[0]*n
        # pre[0]=stones[0]
        # for i in range(1,n):
        #     pre[i]=pre[i-1]+stones[i]
        pre=list(accumulate(stones))
        f=[0]*n
        f[n-1]=pre[n-1]
        for i in range(n-2,0,-1):
            f[i]=max(f[i+1],pre[i]-f[i+1])
        return f[1]
        