/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode l3 = head;
        boolean carryover = false;
        int val3 = 0;

        while (l1 != null || l2 != null || carryover != false) {

            if (l1 != null) {
                val3 += l1.val;
                l1 = l1.next;
            }
            if (l2 != null) {
                val3 += l2.val;
                l2 = l2.next;
            }

            if (carryover == true) {
                val3 += 1;
                carryover = false;
            }

            if (val3 >= 10) {
                val3 -= 10;
                carryover = true;
            }

            l3.next = new ListNode(val3);
            l3 = l3.next;
            val3 = 0;
        }

        return head.next;
    }
}