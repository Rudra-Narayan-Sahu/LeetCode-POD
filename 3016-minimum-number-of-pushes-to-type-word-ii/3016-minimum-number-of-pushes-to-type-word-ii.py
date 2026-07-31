class Solution(object):
    def minimumPushes(self, word):
        dict={}
        for el in word:
            dict[el]=dict.get(el,0)+1
        #print(len(dict))
        freq = sorted(dict.values(), reverse=True)
        total=0
        for i,f in enumerate(freq):
            p=i//8+1
            total+=p*f
        return total