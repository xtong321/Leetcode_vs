"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
2130. Maximum Twin Sum of a Linked List
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.

Input: head = [5,4,2,1]
Output: 6

Input: head = [4,2,2,3]
Output: 7
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        node = self
        while node:
            print("{}, ".format(node.val))
            node = node.next

class Solution(object):    
    def createList(self, array):
        link = ListNode()
        if array:
            link = ListNode(array[0])
         
        pre = link
        for i in range(1, len(array)):
            node = ListNode(array[i])
            pre.next = node
            pre = pre.next
        
        link.print()

        return link

    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        link=[] # stack to save original stack val
        temp=head
        while temp:
            link.append(temp.val)
            temp=temp.next
        N = len(link) # size of link
        temp=head
        idx = 0
        opt_sum = 0
        while temp and idx < N//2:
            val1 = link[idx]
            val2 = link[N-1-idx]
            #temp.val=link.pop()
            opt_sum = max(val1+val2, opt_sum)
            temp=temp.next
            idx = idx + 1
        return opt_sum

        
if __name__ == "__main__":
    #head = [5,4,2,1] # Output: 6
    head = [4,2,2,3] # Output: 7
    the_slo = Solution()
    the_link = the_slo.createList(head)
    print(the_slo.pairSum(the_link))

    