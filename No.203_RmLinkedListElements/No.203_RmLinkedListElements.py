# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head == None:
            return

        pre = head
        while pre and pre.val == val:
            pre = pre.next
        if pre == None:
            return

        ans = pre
        cur = pre.next

        while cur:
            if cur.val == val:
                if cur.next == None:  # the last node
                    pre.next = None
                    cur = None
                    break
                tmp = cur.next
                pre.next = tmp
                cur = tmp
            else:
                pre = pre.next
                cur = cur.next
        return ans
