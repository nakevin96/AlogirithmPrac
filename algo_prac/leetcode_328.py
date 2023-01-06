class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(head):
    if head is None or head.next is None or head.next.next is None:
        return head

    check = True
    pointer = head
    odd_node = ListNode()
    even_node = ListNode()
    result_odd = odd_node
    result_even = even_node
    while pointer:
        if check:
            odd_node.next = pointer
            odd_node = odd_node.next
        else:
            even_node.next = pointer
            even_node = even_node.next

        pointer = pointer.next
        check = not check
    odd_node.next = result_even.next
    return result_odd.next


def print_list(list_name):
    while list_name:
        print(list_name.val)
        list_name = list_name.next


a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)
a.next.next.next = ListNode(4)
a.next.next.next.next = ListNode(5)

print_list(odd_even_list(a))
