class Node:
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne:

    def __init__(self):
        self.head = Node(float('-inf')) # Head of the list(dummy node with negatine infinity)
        self.tail = Node(float('-inf')) # Tail of the list(dummy node with infinity)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_count = {} # HashMap: key -> count
        self.count_node = {}    # HashMap: count -> node
        
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def _add_after(self, node, new_node):
        next_node = node.next
        node.next = new_node
        new_node.prev = node
        new_node.next = next_node
        next_node.prev = new_node

    def inc(self, key: str) -> None:
        if key in self.key_count:
            count = self.key_count[key]
            self.key_count[key] += 1
        else:
            count = 0
            self.key_count[key] = 1
            
        cur_node = self.count_node.get(count, self.head)
        new_count = count + 1
        new_node = self.count_node.get(new_count)
        
        if not new_node:
            new_node = Node(new_count)
            self.count_node[new_count] = new_node
            self._add_after(cur_node, new_node)
            
        new_node.keys.add(key)
        if count > 0:
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove(cur_node)
                del self.count_node[count]

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        
        count = self.key_count[key]
        cur_node = self.count_node[count]
        new_count = count - 1
        
        if new_count == 0:
            del self.key_count[key]
        else:
            self.key_count[key] = new_count
            
        if new_count > 0:
            new_node = self.count_node.get(new_count)
            if not new_node:
                new_node = Node(new_count)
                self.count_node[new_count] = new_node
                self._add_after(cur_node.prev, new_node)
            new_node.keys.add(key)
            
        cur_node.keys.remove(key)
        if not cur_node.keys:
            self._remove(cur_node)
            del self.count_node[count]
        
    def getMaxKey(self) -> str:
        return '' if self.tail.prev == self.head else next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        return '' if self.head.next == self.tail else next(iter(self.head.next.keys))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()