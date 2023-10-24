# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        if not root:
            return result
        
        queue = [root]
        
        while queue:
            level_size = len(queue)
            level = float('-inf')
            for i in range(level_size):
                current = queue.pop(0)
                level = max(level, current.val)
                if current.left:
                    queue.append(current.left)
                    
                if current.right:
                    queue.append(current.right)
            
            result.append(level)
        
        return result