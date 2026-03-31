"""
https://neetcode.io/problems/singlyLinkedList
Design Singly Linked List
Design a Singly Linked List class.
Your LinkedList class should support the following operations:
- LinkedList() will initialize an empty linked list.
- int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
- void insertHead(int val) will insert a node with val at the head of the list.
- void insertTail(int val) will insert a node with val at the tail of the list.
- bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
- int[] getValues() return an array of all the values in the linked list, ordered from head to tail.

Example 1:
Input: 
["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
Output:
[null, null, null, true, [0, 2]]

Example 2:
Input:
["insertHead", 1, "insertHead", 2, "get", 5]
Output:
[null, null, -1]

Note:
The index int i provided to get(int i) and remove(int i) is guaranteed to be greater than or equal to 0.
"""

class Node:
    def __init__(self, val, next=None):        
        self.val = val        
        self.next = next # single link

class LinkedList:
    # - LinkedList() will initialize an empty linked list.
    def __init__(self):
        #raise NotImplementedError        
        self.head = None
        self.arr = [] # for debug
        self.size = 0   # link size
        #self.tail.prev = self.head
    
    # - int get(int i) will return the value of the ith node (0-indexed). If the index is out of bounds, return -1.
    def get(self, index: int) -> int:
        #raise NotImplementedError
        if index < 0 or index > self.size:
            return -1
        # find the node with idx = index
        curr_node = self.head
        curr_idx = 0
        while curr_idx >= 0:
            if curr_idx == index:
                return curr_node.val

            curr_node = curr_node.next
            curr_idx += 1
            if curr_idx >= self.size:
                break        
        return -1

    # - void insertHead(int val) will insert a node with val at the head of the list.
    def insertHead(self, val: int) -> None:
        #raise NotImplementedError        
        new_node = Node(val)
        if self.head:
            next_node = self.head
            self.head = new_node
            self.head.next = next_node
        else:
            self.head = Node(val)
        self.size += 1
        self.arr.insert(0, val)

    # - void insertTail(int val) will insert a node with val at the tail of the list.
    def insertTail(self, val: int) -> None:
        #raise NotImplementedError
        # generate a new node
        new_node = Node(val)

        # find curr_tail node
        tail_node = self.head
        curr_idx = 0
        curr_node = self.head
        while curr_node:
            if curr_node.next == None: # next node is None, it is tail
                tail_node = curr_node
                break
            curr_node = curr_node.next

        tail_node.next = new_node
        self.size += 1
        self.arr.insert(self.size-1, val)


    # - bool remove(int i) will remove the ith node (0-indexed). If the index is out of bounds, return false, otherwise return true.
    def remove(self, index: int) -> bool:
        #raise NotImplementedError
        if index < 0 or index >= self.size:
            return False

        # find the node
        prev_node = self.head
        prev_idx = 0
        while prev_node:
            if prev_idx == index-1: # next node is None, it is tail                
                break
            prev_node = prev_node.next
            prev_idx += 1
        
        if not prev_node:
            return False

        curr_node = prev_node.next        
        prev_node.next = curr_node.next 
        self.size -= 1
        self.arr.pop(index)

        return True

    # - int[] getValues() return an array of all the values in the linked list, ordered from head to tail.
    def getValues(self): # -> List[int]:
        #raise NotImplementedError
        array = []
        curr_idx = 0
        curr_node = self.head
        while curr_node:
            array.append(curr_node.val)
            curr_node = curr_node.next

        return array


if __name__ == "__main__":
    # Input: ["insertHead", 1, "insertTail", 2, "insertHead", 0, "remove", 1, "getValues"]
    # Output: [null, null, null, true, [0, 2]]
    the_list = LinkedList()
    print(the_list.insertHead(1))
    print(the_list.insertTail(2))
    print(the_list.insertHead(0))
    print(the_list.remove(1))
    print(the_list.getValues())

    # Input: ["insertHead", 1, "insertHead", 2, "get", 5]
    # Output: [null, null, -1]
    the_list2 = LinkedList()
    print(the_list2.insertHead(1))
    print(the_list2.insertTail(2))    
    print(the_list2.get(5))