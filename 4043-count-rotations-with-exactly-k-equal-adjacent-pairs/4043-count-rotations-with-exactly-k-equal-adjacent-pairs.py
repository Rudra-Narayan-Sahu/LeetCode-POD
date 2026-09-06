class Solution(object):
    def countRotations(self, s, k):
        total=0
        n=len(s)
        for i in range(len(s)):
            t=s[i:]+s[:i]
            score=0
            for j in range(len(t)-1):
                if t[j]==t[j+1]:
                    score+=1
            if score==k:
                total+=1
        return total

        