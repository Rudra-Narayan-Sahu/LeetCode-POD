class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        memory = dict(knowledge)
        result = []
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                j = i + 1
                while j < n and s[j] != ')':
                    j += 1
                key = s[i+1:j]
                result.append(memory.get(key, '?'))
                i = j + 1
            else:
                result.append(s[i])
                i += 1  
        return "".join(result)