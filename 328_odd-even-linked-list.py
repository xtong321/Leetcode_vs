"""
https://leetcode.com/problems/odd-even-linked-list/description/?envType=study-plan-v2&envId=leetcode-75
328. Odd Even Linked List

Given the head of a singly linked list, group all the nodes with 
odd indices together followed by the nodes with even indices, 
and return the reordered list.

The first node is considered odd, and the second node is even, and so on.
Note that the relative order inside both the even and odd 
groups should remain as it was in the input.

You must solve the problem in O(1) extra space 
complexity and O(n) time complexity.

Example-1:
Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example-2:
Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_from_list(arr):
        if not arr:
            return None
        N = len(arr)
        head = ListNode(arr[0])
        curr = head
        for k in range(0, N-1):
            curr.next = ListNode(arr[k+1])
            curr = curr.next

        return head     
    
    # 打印结果链表
    def print(self):
        cur = self
        while cur:
            print(cur.val, end=" -> " if cur.next else "")
            cur = cur.next
        print("\n")

class Solution(object):
    def fun1(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None

        size = 0 # size of original link
        odd_link = head
        even_link = head.next
        odd_head = odd_link
        even_head = even_link
        
        index = 2
        cur = head.next.next
        while cur:
            if index % 2 == 0:
                odd_link.next = cur
                odd_link = odd_link.next
            else:
                even_link.next = cur
                even_link = even_link.next

            cur = cur.next            
            index = index + 1

        odd_link.next = None
        even_link.next = None
        #odd_head.print()
        #even_head.print()
        odd_link.next = even_head
        #odd_head.print()
        return odd_head
    
    def fun2(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        evenHead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head


if __name__ == "__main__":
    # Input: head = [1,2,3,4,5], Output: [1,3,5,2,4]
    """
    head = [1,2,3,4,5]
    print(head)    
    org_link = ListNode.create_from_list(head)
    #new_link1 = Solution().fun1(org_link)
    #new_link1.print()
    #new_link2 = Solution().fun2(org_link)    
    #new_link2.print()
    """

    
    # Input: head = [2,1,3,5,6,4,7], Output: [2,3,6,7,1,5,4]
    head = [2,1,3,5,6,4,7]
    print(head) 
    org_link = ListNode.create_from_list(head)
    #new_link1 = Solution().fun1(org_link)
    #new_link1.print()
    new_link2 = Solution().fun2(org_link)
    new_link2.print()
    