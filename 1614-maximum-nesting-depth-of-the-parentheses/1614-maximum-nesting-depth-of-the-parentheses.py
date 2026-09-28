class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx=0
        total=0
        for i,ch in enumerate(s):
            if ch=='(':
                total+=1
                mx=max(mx,total)
            elif ch==')':
                total-=1
        return mx


        