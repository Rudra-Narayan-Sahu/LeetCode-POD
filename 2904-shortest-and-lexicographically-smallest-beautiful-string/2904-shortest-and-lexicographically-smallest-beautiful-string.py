class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        count=0
        for ch in s:
            if ch=='1':
                count+=1
        if count<k:
            return ""
        left=0
        oncs_count=0
        res=""
        for right in range(len(s)):
            if s[right]=='1':
                oncs_count+=1
            while oncs_count==k:
                sub=s[left:right+1]
                if not res or len(sub) < len(res) or (len(sub) == len(res) and sub < res):
                    res=sub
                if s[left]=='1':
                    oncs_count-=1
                left+=1
        return res
    def Compare(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        return s1>s2
