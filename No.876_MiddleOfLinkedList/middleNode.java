/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode middleNode(ListNode head) {
        
        if(head.next == null)
            return head;        
        
        ListNode mid = head.next;
        int step = 1;
        head = head.next;
        
        while(head.next != null)
        {
            head = head.next;
            step += 1;
            if(step%2==1)
                mid = mid.next;
        }
        
        return mid;
    }
}