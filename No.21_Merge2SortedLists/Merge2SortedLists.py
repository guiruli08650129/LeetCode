# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        Head = ListNode(0)
        ptr = Head

        while p1 != None and p2 != None:
            if p1.val > p2.val:
                ptr.next = ListNode(p2.val)
                ptr = ptr.next
                p2 = p2.next
            elif p1.val < p2.val:
                ptr.next = ListNode(p1.val)
                ptr = ptr.next
                p1 = p1.next
            else:
                ptr.next = ListNode(p1.val)
                ptr = ptr.next
                p1 = p1.next
        if p1 != None:
            ptr.next = p1
        if p2 != None:
            ptr.next = p2

        return Head.next
