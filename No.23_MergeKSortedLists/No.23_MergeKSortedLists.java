/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if(lists.length == 0)
            return null;
        if(lists.length == 1)
            return lists[0];
        
        ListNode ans = merge2list(lists[0], lists[1]);

        for(int i = 2 ; i < lists.length ; i++)
        {
            ans = merge2list(ans, lists[i]);            
        }
            
        return ans;
    }
    private ListNode merge2list(ListNode l1, ListNode l2)
    {
        ListNode ptr = new ListNode(0);
        ListNode head = ptr;
        
        while(l1 != null && l2 != null)
        {
            if(l1.val > l2.val)
            {
                ptr.next = l2;
                l2 = l2.next;
            }
            else
            {
                ptr.next = l1;
                l1 = l1.next;
            }
            ptr = ptr.next;            
        }
        
        if(l1 == null)
            ptr.next = l2;
        if(l2 == null)
            ptr.next = l1;
        
        return head.next;
    }
}