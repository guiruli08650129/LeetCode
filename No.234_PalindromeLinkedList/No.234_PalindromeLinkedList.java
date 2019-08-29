class Solution {
    public boolean isPalindrome(ListNode head) {
        
        if(head == null)
            return true;
        
        int count = 0;
        ListNode ptr = head;
        while(ptr != null)
        {
            ptr = ptr.next;
            count++;
        }
        int mid = count/2;
        System.out.println(mid);
        
        ListNode temp = head;
        ListNode pad = new ListNode(-1);
        
        for(int i = 0 ; i < mid ; i++)
        {
            temp = temp.next;
            head.next = pad;
            pad = head;
            head = temp;
            System.out.printf("%d %d %d\n", temp.val, head.val, pad.val);
        }
        if(count % 2 == 1)
            head = head.next;
        
        while(pad != null && head != null)
        {
            if(pad.val == head.val)
            {
                pad = pad.next;
                head = head.next;
            }
            else
                return false;
        }
        return true;        
    }
}