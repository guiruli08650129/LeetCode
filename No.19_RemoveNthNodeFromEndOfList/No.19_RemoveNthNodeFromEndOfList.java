class Solution {
	public ListNode removeNthFromEnd(ListNode head, int n) {
		int count = 0;
		ListNode p1 = head;
		ListNode p2 = head;
		ListNode pre = null;

		if (head.next == null)
			return null;

		while (n > 0) {
			p1 = p1.next;
			n -= 1;
		}
        
		if(p1 == null)
			return p2.next;
        
		
		while (p1 != null) {
			p1 = p1.next;
			pre = p2;
			p2 = p2.next;
		}
		pre.next = p2.next;

		return head;

	}
}