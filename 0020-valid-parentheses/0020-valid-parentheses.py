class Solution(object):
  def isValid(self, s):
    stack = []
    for ch in s:
      if ch == "(" or ch == "{" or ch == "[":
        stack.append(ch)
      else:
        if not stack:
          return False
        elif (
            (stack[-1] == "(" and ch == ")")
            or (stack[-1] == "[" and ch == "]")
            or (stack[-1] == "{" and ch == "}")
        ):
          stack.pop()
        else:
          return False

    return len(stack) == 0