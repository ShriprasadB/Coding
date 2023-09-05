"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dict1 = {None: None}
        
        cur = head
        
        while cur:
            L = Node(cur.val)
            dict1[cur] = L
            cur = cur.next
            
        cur = head
        while cur:
            dict1[cur].next = dict1[cur.next]
            dict1[cur].random = dict1[cur.random]
            cur = cur.next
            
        return dict1[head]
        