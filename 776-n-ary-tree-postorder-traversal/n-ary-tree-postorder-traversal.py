"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root==None:
            return []
        stack=[root]
        lst=[]
        while stack:
            node=stack.pop()
            lst.append(node.val)
            for child in node.children:
                stack.append(child)
        return lst[::-1]

        
        