# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return 
        queue=[]
        queue.append(root)
        while queue:
            size=len(queue)
            for i in range(size):
                temp=queue.pop()
                temp.left,temp.right=temp.right,temp.left
                # if temp.left is not None and temp.right is not None:
                #     temp.left,temp.right=temp.right,temp.left
                # elif temp.left is not None:
                #     temp.right=temp.left
                # elif temp.right is not None:
                #     temp.left=temp.right
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return root