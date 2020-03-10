class Node:
    '''双向链表的节点'''
    __slots__ = ('prev', 'next', 'key', 'val')


class HashLinkedList:
	'''双向链表+哈希表实现LRU'''

    def __init__(self, capacity):
        self.__root = root = Node()
        root.prev = root.next = root
        self.capacity = capacity
        self.map = {}

    def get(self, key):
        if key not in self.map:
            return -1
        self.move_to_head(self.map[key])
        return self.map[key].val

    def put(self, key, val):
        if key in self.map:
            move_to_head(self.map[key])
            self.map[key].val = val
        else:
            x = Node()
            x.key = key
            x.val = val
            self.map[key] = x
            self.add_head(x)
            if len(self.map) > self.capacity:
                self.remove_tail()

    def move_to_head(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
        head = self.__root.next
        x.prev = self.__root.next
        self.__root.next = x
        x.next = head
        head.prev = x

    def add_head(self, x):
        head = self.__root.next
        x.prev = self.__root.next
        self.__root.next = x
        x.next = head
        head.prev = x

    def remove_tail(self):
        tail = self.__root.prev
        self.__root.prev = tail.prev
        tail.prev.next = self.__root
        del self.map[tail.key]

    def __repr__(self):
        node = self.__root.next
        strs = str()
        while node != self.__root:
            strs += str((node.key, node.val))
            node = node.next
        return strs


if __name__ == '__main__':
    lru = HashLinkedList(3)
    lru.put(7, 70)
    lru.put(0, 0)
    print(lru.get(7))
    lru.put(1, 10)
    print(lru.get(0))
    print(lru)
    lru.put(3, 30)
    print(lru)
