class Solution(object):
    def maximumLengthSubstring(self, s):
        n=len(s)
        memory={}
        left=0
        m=0
        for right,ch in enumerate(s):
            memory[ch]=memory.get(ch,0)+1
            while memory[ch]>2:
                memory[s[left]]-=1
                left+=1
            
            m=max(m,right-left+1)
        return m            
            

        