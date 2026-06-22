class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        for el in costs:
            if el>coins:
                break
            else:
                coins-=el
                count+=1
        return count

        