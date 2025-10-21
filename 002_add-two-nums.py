"""
add two nums
定义这样的一个链表，链表的每个节点都存有一个0-9的数字，把链表当成数字，
表头为高位，表尾为地位。如1->2->3表示321，现在要对两个这样的链表求和。
注意点：
数字的高低位，应该从从地位向高位进位
有多种情况要考虑，如链表长度是否相等、是否进位等
例子：
输入: (2 -> 4 -> 3) + (5 -> 6 -> 4) 输出: 7 -> 0 -> 8

https://leetcode.cn/problems/add-two-numbers/
"""

from typing import AnyStr


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def myPrint(self):
        node = self
        while node:
            print(node.val)
            node = node.next
        '''
        print(self.val)
        if self.next:
            self.next.myPrint()
        '''


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            cur.val += self.addTwoNodes(l1,l2)
            if cur.val >= 10:
                cur.val -= 10
                cur.next = ListNode(1)
            else:
                #check if there is need to make the next node
                if l1 and l1.next or l2 and l2.next:
                    cur.next = ListNode(0)
            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return result

    def addTwoNodes(self, n1, n2):
        if not n1 and not n2:
            #cannot happen, ignore it
            None
        if not n1:
            return n2.val
        if not n2:
            return n1.val
        return n1.val + n2.val

    def addTwoNumbers2(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        ans = result
        overflow = 0
        temp_ans = 0
        while l1 or l2:            
            temp_ans = self.addTwoNodes(l1, l2) + overflow
            if temp_ans >= 10:
                overflow = 1
                temp_ans -= 10
            else:
                overflow = 0
            ans.val = temp_ans
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if l1 or l2 or overflow>0:
                ans.next = ListNode(overflow)          
                ans = ans.next

        return result # return list header
   

if __name__ == "__main__":
    list1 = ListNode(9)
    list1.next = ListNode(9)
    list1.next.next = ListNode(9)
    list1.next.next.next = ListNode(9)
    list1.next.next.next.next = ListNode(9)
    list1.next.next.next.next.next = ListNode(9)
    list1.next.next.next.next.next.next = ListNode(9)
    
    list2 = ListNode(9)
    list2.next = ListNode(9)
    list2.next.next = ListNode(9)
    list2.next.next.next = ListNode(9)

    print('list1: '), list1.myPrint()
    print('list2: '), list2.myPrint()

    print('list1 + list2: ')
    print(Solution().addTwoNumbers2(list1, list2).myPrint()) # [8,9,9,9,0,0,0,1]
    #print(Solution().addTwoNumbers(list, ListNode(1)).myPrint()) 
