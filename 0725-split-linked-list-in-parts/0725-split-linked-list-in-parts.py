# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, cur1):
        count = 0
        while cur1:
            cur1 = cur1.next
            count += 1
        
        return count

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        answer = []
        cur, cur1 = head, head
        
        n = self.length(cur1)

        extras = n % k
        split_len = n//k

        for i in range(k):
            answer.append(cur)
            for j in range(split_len - 1 + (1 if extras else 0)):
                if not cur:
                    break
                cur = cur.next
                
            if extras:
                extras -= 1
                
            if cur:
                temp = cur.next
                cur.next = None
                cur = temp
        
        return answer