class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        res={}
        for i in range(len(s)-minSize+1):
            word=s[i:i+minSize]
            if len(set(word))<=maxLetters:
                res[word]=res.get(word,0)+1
        return max(res.values()) if res else 0

