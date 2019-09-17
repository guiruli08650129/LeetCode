class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        ans = head.next
        newHead = head.next
        hold = head.next.next
        while hold != None:
            head.next = None
            newHead.next = head
            head.next = hold.next
            
            if hold.next != None:
                head = hold
                newHead = hold.next
                hold = hold.next.next
            else:                
                break
        
        if head.next != None and not hold:
            newHead.next = head
            head.next = None    
        if head.next == None:
            head.next = hold        
            
        return ans