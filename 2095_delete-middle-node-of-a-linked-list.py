"""
2095. Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, 
and return the head of the modified linked list.
The middle node of a linked list of size n is the 
⌊n / 2⌋th node from the start using 0-based indexing, 
where ⌊x⌋ denotes the largest integer less than or equal to x.
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


class Solution(object):
    def deleteMiddle1(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return None

        N = 0 # the size of list
        curr = head
        while curr:
            N += 1
            curr = curr.next            

        Mid = N//2        
        prev, k, post = 0, 0, 0
        curr = head
        for i in range(0, N):
            prev_node = curr
            curr_node = curr.next
            post_node = curr_node.next
            if i+1 == Mid:
                break
            curr = curr.next

        prev_node.next = post_node

        return head

    def deleteMiddle2(self, head: ListNode) -> ListNode:
        # 如果只有一个节点，删除后返回 None
        if not head or not head.next:
            return None
        
        slow, fast = head, head
        prev = None
        
        # 快慢指针遍历
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        # 删除中间节点
        prev.next = slow.next

        return head

## test
if __name__ == "__main__":
    #Input: head = [1,3,4,7,1,2,6], Output: [1,3,4,1,2,6]
    #head = [1,3,4,7,1,2,6]
    head = ListNode.create_from_list([1,3,4,7,1,2,6])
    head1 = ListNode(1, ListNode(3, ListNode(4, ListNode(7, ListNode(1, ListNode(2, ListNode(6)))))))
    #Solution().deleteMiddle1(head)
    sol = Solution()
    new_head = sol.deleteMiddle1(head)

    # 打印结果链表
    cur = new_head
    while cur:
        print(cur.val, end=" -> " if cur.next else "")
        cur = cur.next

    #Input: head = [1,2,3,4], Output: [1,2,4]
    head = [1,2,3,4]
    #Solution().deleteMiddle1(head)

    #Input: head = [2,1], Output: [2]
    head = [2,1]
    #Solution().deleteMiddle1(head)
