# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = [root]
        graph = collections.defaultdict(list)

        while q:
            node = q.pop(0)

            if node.left:
                q.append(node.left)
                graph[node].append(node.left)
                graph[node.left].append(node)

            if node.right:
                q.append(node.right)
                graph[node].append(node.right)
                graph[node.right].append(node)

        q = [(0, target)]
        answer = []
        visit = set()
        while q:
            distance, node = q.pop(0)
            visit.add(node)

            if distance == k:
                answer.append(node.val)
            
            for nei in graph[node]:
                if nei not in visit:
                    q.append((1 + distance, nei))
        
        return answer
            