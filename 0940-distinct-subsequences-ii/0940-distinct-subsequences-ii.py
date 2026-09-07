class Solution(object):
    
    def distinctSubseqII(self, s):
        MOD=10**9+ 7
        total=0
        dp=[0]*26
        for ch in s:
            ch=ord(ch)-97
            new=total+1-dp[ch]
            total=(total+new)%MOD
            dp[ch]=(dp[ch]+new)%MOD
        return total
        