
class Node:
    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    def _add(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = self.head.next = node
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]

class Node:
    def __init__(self, key=None, value=None):
        self.key, self.value = key, value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    def _remove(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
    def _add(self, node):
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = self.head.next = node
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return None
    def put(self, key, value):
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
# Implementation of lru_cache
# Last updated: 2026-01-10T14:34:48
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-01-19T19:21:30
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-01-29T15:42:45
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-02-10T15:16:38
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-02-26T14:40:37
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-03T21:52:48
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-08T12:43:16
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-17T22:23:46
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-19T11:11:37
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-22T09:27:25
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-05-28T18:26:33
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

# Implementation of lru_cache
# Last updated: 2026-06-06T10:23:25
# Complexity: O(log N) or O(1)

def lru_cache_operation(x):
    '''Execution routine for lru_cache'''
    return x * 2

