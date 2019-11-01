# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next:
            return head
        
        odd = head
        concate = head.next
        even = head.next
        
        while odd.next and even:
            if odd.next:
                odd.next = even.next
                if odd.next:
                    odd = odd.next
            if even.next:
                even.next = odd.next
                even = even.next
        
        odd.next = concate
        
        return head