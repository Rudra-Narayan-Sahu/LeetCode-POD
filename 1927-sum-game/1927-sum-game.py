class Solution:
    def sumGame(self, num: str) -> bool:
        n=len(num)
        mid=n//2
        left_s,right_s=num[:mid],num[mid:]
        s1=self.sumCal(left_s)
        s2=self.sumCal(right_s)
        q1=left_s.count('?')
        q2=right_s.count('?')
         # if q1>q2:
         #     return True
         # elif q1=q2:
         #     if s1==s2:
         #         return False
         #     elif s1>s2:
         #         return True
         # else:#q1<q2
         #     if q1==0:
         #         if s1-s2==(9/(2*q2)):
         #             return False
         #         elif s1-s2>(9/(2*q2)):
         #             return True
         #         else:
         #             return True
        if 2*(s1-s2)==9*(q2-q1):
            return False

        return True
    def counter(self,num:str)->int:
        c=0
        for ch in num:
            if ch=='?':
                c+=1
        return c
    def sumCal(self,num:str)->int:
        s=0
        for el in num:
            if el!='?':
                s+=int(el)
            else:
                continue
        return s

