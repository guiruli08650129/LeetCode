# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        c = set()
        p = head
        pre = ListNode(-1)
        pre.next = head
        while p:
            if p.val not in c:
                c.add(p.val)
                p = p.next
                pre = pre.next
            else:
                pre.next = p.next
                p = p.next
        return head