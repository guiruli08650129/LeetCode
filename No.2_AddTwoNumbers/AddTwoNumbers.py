# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        s1 = ""
        s2 = ""

        while(p1 != None):
            s1 += str(p1.val)
            p1 = p1.next

        while(p2 != None):
            s2 += str(p2.val)
            p2 = p2.next

        s = str(int(s1[::-1]) + int(s2[::-1]))[::-1]

        out = ListNode(int(s[0]))
        ptr = out
        for w in s[1:]:
            w = int(w)
            ptr.next = ListNode(w)
            ptr = ptr.next

        return out
