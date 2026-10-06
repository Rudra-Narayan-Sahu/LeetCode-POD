class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=deque()
        for ch in s:
            if ch=='(':
                stack.append(ch)
            else:
                if len(stack)>0:
                    if stack[-1]=='(':
                        stack.pop()
                    else:
                        stack.append(ch)
                else:
                    stack.append(ch)
        return len(stack)