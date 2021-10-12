# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li1=[]
        self.li2=[]
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.dfs(root1,self.li1)
        self.dfs(root2,self.li2)
        return self.li1==self.li2
    def dfs(self,root,li):
        
        #base
        if root.left is None and root.right is None:
            li.append(root.val)
            return
            
        #logic
        if root.left:
            self.dfs(root.left,li)
        if root.right:
            self.dfs(root.right,li)
        