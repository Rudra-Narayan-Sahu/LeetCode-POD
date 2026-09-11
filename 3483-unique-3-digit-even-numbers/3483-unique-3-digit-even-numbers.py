class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        res=set()
        n=len(digits)
        for i in range(n):#100th placee
            if digits[i]==0:
                continue
            for j in range(n):#10th place
                if i==j:
                    continue
                for k in range(n):#once place
                    if k==i or k==j:
                        continue
                    if digits[k]%2==0:
                        d=digits[i]*100+digits[j]*10+digits[k]
                        res.add(d)
        return len(res)