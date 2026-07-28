class Solution(object):
    def smallestPalindrome(self, s):
        n=len(s)
        mid=n//2
        left="".join(sorted(s[:mid]))
        middle=s[mid] if n%2!=0 else ""
        return left+middle+left[::-1]

        