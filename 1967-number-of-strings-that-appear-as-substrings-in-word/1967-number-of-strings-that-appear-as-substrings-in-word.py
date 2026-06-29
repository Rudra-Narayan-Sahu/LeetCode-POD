class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for el in patterns:
            if el in word:
                count+=1
        return count
        