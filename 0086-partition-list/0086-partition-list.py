# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        if not head:
            return head

        cur = head
        first = ListNode(None)
        second = ListNode(None)
        head1 = first
        head2 = second

        while cur:
            if cur.val >= x:
                if not second:
                    second = ListNode(cur.val)
                else:
                    second.next = ListNode(cur.val)
                    second = second.next
            else:
                if not first:
                    first = ListNode(cur.val)
                else:
                    first.next = ListNode(cur.val)
                    first = first.next

            cur = cur.next

        if head2.next:
            first.next = head2.next

        return head1.next