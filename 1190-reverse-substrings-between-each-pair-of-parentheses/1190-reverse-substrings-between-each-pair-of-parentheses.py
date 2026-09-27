from collections import deque
class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack=deque()
        for i,ch in enumerate(s):
            if ch==')':
                sub=[]
                while stack and stack[-1]!='(':
                    sub.append(stack.pop())
                if stack and stack[-1]=='(':
                    stack.pop()
                for el in sub:
                    stack.append(el)
            else:
                stack.append(ch)
        return "".join(stack)

        