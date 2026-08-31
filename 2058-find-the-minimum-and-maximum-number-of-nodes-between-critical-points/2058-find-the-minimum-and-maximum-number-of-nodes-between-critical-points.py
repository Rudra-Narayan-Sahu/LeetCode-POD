# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head.next
        prev=head
        local=[]
        count=1
        while curr.next:
            nexxt=curr.next
            if curr.val<prev.val and curr.val<nexxt.val:#Local Minima
                local.append(count)
            elif curr.val>prev.val and curr.val>nexxt.val:
                local.append(count)
            count+=1
            prev=curr
            curr=curr.next
        if len(local)<2:
            return [-1,-1]
        else:
            idx=float('inf')
            for i in range(len(local)-1):
                idx=min(idx,local[i+1]-local[i])

            return [idx,abs(local[-1]-local[0])]


            


        