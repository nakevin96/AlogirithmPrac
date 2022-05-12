# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = deque()
        while head:
            val_list.append(head.val)
            head = head.next

        for i in range(len(val_list) // 2):
            if val_list.pop() != val_list.popleft():
                return False

        return True