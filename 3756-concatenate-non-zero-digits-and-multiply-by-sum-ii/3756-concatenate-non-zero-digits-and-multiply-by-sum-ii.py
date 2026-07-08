class Solution(object):
    def sumAndMultiply(self, s, queries):
        ans=[]
        prefix=[]
        numbers=[]
        k=[]
        sumx=0
        temp_x=0
        co=0
        MOD=10**9+7
        for ch in s:
            d=int(ch)
            sumx+=d
            prefix.append(sumx)
            if d!=0:
                temp_x = (temp_x * 10 + d) % MOD
                co+=1
            numbers.append(temp_x)
            k.append(co)
        pow10=[1]*(co + 1)
        for i in range(1, co + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD
        for l,r in queries:
            if l==0:
                sum_range=prefix[r]
                lc=0
                ln=0
            else:
                sum_range=prefix[r]-prefix[l-1]#computed the sum of l->r 
                lc=k[l-1]
                ln=numbers[l-1]
            rc=k[r]
            length=rc-lc
            if length == 0:
                ans.append(0)
                continue
            x = (numbers[r]-ln*pow10[length]) % MOD
            ans.append((x*sum_range) % MOD)
        return ans

            
        