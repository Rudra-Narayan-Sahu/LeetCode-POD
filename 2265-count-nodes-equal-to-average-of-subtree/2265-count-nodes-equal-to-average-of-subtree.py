# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    res=0
    def averageOfSubtree(self, root):
        self.helper(root)
        return self.res
    def helper(self,root):
        if not root:
            return 0,0
        ls,lc=self.helper(root.left)
        rs,rc=self.helper(root.right)
        total_sum=ls+rs+root.val
        total_count=lc+rc+1
        avg=total_sum//total_count
        if avg==root.val:
            self.res+=1
        return total_sum,total_count
        

        

    
        