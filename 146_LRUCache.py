"""
lru-cache

请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。
实现 LRUCache 类：
LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。
函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。

示例：
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

Idea:
1) using a double linked list + hashmap, which gives O(1) time for both get() and put() operations:
2) for each valid get and put, move the key to top. and update the link
"""

class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node

        # Dummy head and tail for the doubly linked list
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    # Helper: remove a node from the linked list
    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    # Helper: add node right after head (most recent)
    def _add_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    # Move an existing node to head (most recently used)
    def _move_to_head(self, node):
        self._remove(node)
        self._add_to_head(node)

    # Remove the least recently used node (at tail.prev)
    def _pop_tail(self):
        node = self.tail.prev
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)
            if len(self.cache) > self.capacity:
                # Evict LRU
                lru = self._pop_tail()
                del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

### my implementation
class Node2():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node (not value)

        self.head = Node2()
        self.tail = Node2()
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove one node
    def _remove(self, node):        
        prev_node = node.prev
        next_node = node.next
        prev_node.next = node.next
        next_node.prev = node.prev
        #del self.cache[key]    

    # add a node to head
    def _add_to_head(self, node):
        # 1) remove the node from bi-link
        # 2) add the node to head of bi-link        
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node        
        self.head.next = node
            
    # move a node to head
    def _move_to_head(self, node):
        # 1) remove the node from bi-link
        # 2) add the node to head of bi-link        
        self._remove(node)
        self._add_to_head(node)

    # remove the tail
    def _pop_tail(self):
        node = self.tail.prev
        #self.tail.prev = node.prev
        #node.prev.next = self.tail
        self._remove(node)
        return node
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            #move the node to head
            self._move_to_head(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        # if already exist, update and move to head
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node2(key, value)
            self.cache[key] = node
            self._add_to_head(node)
            if len(self.cache) > self.capacity:
                lru = self._pop_tail()
                del self.cache[lru.key]


### test code
if __name__ == "__main__":
    lru = LRUCache2(2)
    lru.put(1, 1)  # cache = {1=1}
    lru.put(2, 2)  # cache = {1=1, 2=2}
    print(lru.get(1))  # 1 (moves key=1 to most recent)
    lru.put(3, 3)      # evicts key=2, cache = {1=1, 3=3}
    print(lru.get(2))  # -1 (not found)
    lru.put(4, 4)      # evicts key=1, cache = {3=3, 4=4}
    print(lru.get(1))  # -1
    print(lru.get(3))  # 3
    print(lru.get(4))  # 4