# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ""
        p = head
        while p:
            s += str(p.val)
            p = p.next
        return int(s, 2)
