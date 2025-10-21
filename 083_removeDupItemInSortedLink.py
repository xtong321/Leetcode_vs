"""
Remove Duplicates from Sorted List
删除一个有序链表中重复的元素，使得每个元素只出现一次。
注意点：
无
例子：
输入: 1->1->2->3->3
输出: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

    def my_print(self):
        print(self.val)
        #if self.next:
        #    print(self.next.val)
        cur = self.next
        while cur:
            print(cur.val)
            cur = cur.next

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            curr = curr.next

        return head
        
if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(1)
    n3 = ListNode(1)
    n4 = ListNode(2)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    r = Solution().deleteDuplicates(n1)
    r.my_print()