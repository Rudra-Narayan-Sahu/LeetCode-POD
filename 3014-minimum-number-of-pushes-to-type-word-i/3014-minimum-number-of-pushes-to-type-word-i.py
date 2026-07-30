class Solution(object):
    def minimumPushes(self, word):
        n=len(word)
        cost=1
        total=0
        for i in range(1,n+1):
            if i<=8:
                total+=1
            if i>8 and i<=16:
                total+=2
            elif i>16 and i<=24:
                total+=3
            elif i>24 and i<=26:
                total+=4
        return total
                
        
        