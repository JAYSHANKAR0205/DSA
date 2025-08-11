# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        q=deque([root])
        level=0
        while q:
            
            level+=1
            for i in range(len(q)):
                node=q.popleft()
                if node.left==None and node.right==None:
                    return level
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
        return level
        