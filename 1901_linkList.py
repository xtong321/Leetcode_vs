# 链节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 链表类
class LinkList:
    def __init__(self):
        self.head = None


# 根据 data 初始化一个新链表
def create(self, data):
    if data is None:
        return

    node = ListNode(data[0])
    self.head = node
    cur = self.head
    for i in range(1, len(data)):
        node = ListNode(data[i])
        cur.next = node
        cur = cur.next

    return self.head

# 获取线性链表长度
def length(self):
    length = 0
    cur = self.head
    while cur:
        length += 1
        cur = cur.next

    return length

# 查找元素：在链表中查找值为 val 的元素
def find(self, val):
    if not self.head:
        return None
    
    cur = self.head
    while cur:
        if val == cur.val:
            return cur
        cur = cur.next
    
    return None

# 链表头部插入元素
def insertFront(self, val):
    node = ListNode(val)
    node.next = self.head
    self.head = node


# 链表尾部插入元素
def insertRear(self, val):
    node = ListNode(val)
    cur = self.head
    while cur.next:
        cur = cur.next

    cur.next = node

# 在链表第 i 个链节点之前插入值为 val 的链节点
def insertInside(self, index, val):
    node = ListNode(val)
    cur = self.head
    count = 0
    while cur and count < index - 1:
        count += 1
        cur = cur.next
    if not cur:
        return 'Error'

    node.next = cur.next
    cur.next = node
    
# 改变元素：将链表中第 i 个元素值改为 val
def change(self, index, val):
    cur = self.head
    count = 0
    while cur and count < index:
        count += 1
        cur = cur.next
    
    if not cur:
        return 'Error'
    cur = cur.next
    cur.val = val
    

# 链表头部删除元素
def removeFront(self):
    cur = self.head
    self.head = cur.next

    """
    if self.head:
        self.head = self.head.next
    """

# 链表尾部删除元素
def removeRear(self):
    cur = self.head
    next = cur.next
    while next:
        cur = next
        next = next.next

    cur.next = None
    """
    if not self.head or not self.head.next:
        return 'Error'

    cur = self.head
    while cur.next.next:
        cur = cur.next
    cur.next = None
    """

# 链表中间删除元素
def removeInside(self, index):
    cur = self.head
    count = 0
    while cur and count < index-1:
        count += 1
        cur = cur.next
    
    if not cur:
        return 'Error'
    
    del_node = cur.next
    cur.next = del_node.next
    #cur.next = cur.next.next

"""
My design
"""
class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        idx = 0
        cur = self.head
        while idx < index - 1:
            cur = cur.next

        if not cur:
            return 'Error'

        return cur.val
        

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head.next
        self.head = node
        

    def addAtTail(self, val: int) -> None:
        idx = 0
        cur = self.head
        while cur:
            cur = cur.next

        node = ListNode(val)
        cur.next = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        idx = 0
        cur = self.head
        while idx < index - 1:
            cur = cur.next

        if not cur:
            return 'Error'

        node = ListNode(val)
        node.next = cur.next
        cur.next = node
        

    def deleteAtIndex(self, index: int) -> None:
        idx = 0
        cur = self.head
        while cur and idx < index - 1:
            cur = cur.next

        if not cur:
            return 'Error'

        node = cur.next
        cur.next = node.next
        

# if __name__ == '__main__':
#     obj = MyLinkedList()
#     param_1 = obj.get(index)
#     obj.addAtHead(val)
#     obj.addAtTail(val)
#     obj.addAtIndex(index,val)
#     obj.deleteAtIndex(index)
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)