class Solution(object):
    def countRotations(self, s, k):
        total=0
        n=len(s)
        for i in range(n-1):
            if s[i]==s[i+1]:
                total+=1
        if s[-1]==s[0]:
            total+=1
        if k==total:
            return n-total
        elif k==total-1:
            return total
        else:
            return 0

        
        
        