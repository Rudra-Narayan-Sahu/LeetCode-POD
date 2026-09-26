class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        val=tickets[k]
        total=0
        for i,el in enumerate(tickets):
            if i <= k:
                total += min(el, val)
            else:
                total += min(el, val - 1)
        return total


        