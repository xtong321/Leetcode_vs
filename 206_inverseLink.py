"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""

# Definition for singly-linked list.
class ListNode:
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
        list = ListNode()
        if array:
            list = ListNode(array[0])
         
        pre = list
        for i in range(1, len(array)):
            node = ListNode(array[i])
            pre.next = node
            pre = pre.next
        
        list.print()

        return list

    def reverseList(self, array):
      
        # build a list
        head = self.createList(array)
        head.print()

        inverseLink = []
        stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        if stack:
            top = stack.pop()
            inverseLink = ListNode(top)
        
        pre = inverseLink
        while stack:
            top = stack.pop()
            node = ListNode(top)
            pre.next = node
            pre = pre.next

        inverseLink.print()

        return inverseLink

    
    # just revise val, not reverse pointer
    def reverseList2(self, head):
        link=[] # stack to save original stack val
        temp=head
        while temp:
            link.append(temp.val)
            temp=temp.next
        temp=head
        while temp:
            temp.val=link.pop()
            temp=temp.next
        return head

    def reverseList2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p, rev = head, None
        while p:
            rev, rev.next, p = p, rev, p.next
        return rev

        """
        双指针法
        class Solution {
        public:
            ListNode* reverseList(ListNode* head) {
                ListNode* temp; // 保存cur的下一个节点
                ListNode* cur = head;
                ListNode* pre = NULL;
                while(cur) {
                    temp = cur->next;  // 保存一下 cur的下一个节点，因为接下来要改变cur->next
                    cur->next = pre; // 翻转操作
                    // 更新pre 和 cur指针
                    pre = cur;
                    cur = temp;
                }
                return pre;
            }
        };
        """

if __name__ == "__main__":
    Solution().reverseList([1,2,3,4,5])