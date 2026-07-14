class Solution(object):
    def sequentialDigits(self, low, high):
        n=len(str(high))
        seq=[]
        res=[]
        s="123456789"
        for l in range(len(str(low)),len(str(high))+1):
            for i in range(10-l):
                num=int(s[i:i+l])
                seq.append(num)
        for el in seq:
            if el<=high and el>=low:
                res.append(el)
            else:
                continue
        return res




        