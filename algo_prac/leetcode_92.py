# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        if left == right:
            return head

        prev, curr, count = None, head, 1

        while count != left:
            prev, curr = curr, curr.next
            count += 1

        last, switch1, switch2 = curr, curr, curr.next

        while count != right:
            switch2.next, switch1, switch2 = switch1, switch2, switch2.next
            count += 1

        if prev:
            prev.next = switch1
        else:
            head = switch1
        last.next = switch2

        return head