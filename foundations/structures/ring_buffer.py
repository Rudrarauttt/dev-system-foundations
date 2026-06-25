
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    def append(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity
    def get_all(self):
        return [self.buffer[(self.head + i) % self.capacity] for i in range(self.size)]

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
    def append(self, item):
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        if self.size < self.capacity:
            self.size += 1
        else:
            self.head = (self.head + 1) % self.capacity
    def get_all(self):
        return [self.buffer[(self.head + i) % self.capacity] for i in range(self.size)]
# Implementation of ring_buffer
# Last updated: 2026-01-22T20:54:44
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-02-15T12:34:15
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-04-07T10:36:43
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-04-10T11:14:49
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-05-05T12:07:40
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-05-31T22:29:30
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-06-06T16:53:45
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-06-18T13:14:48
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-06-21T11:05:28
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

# Implementation of ring_buffer
# Last updated: 2026-06-25T15:34:27
# Complexity: O(log N) or O(1)

def ring_buffer_operation(x):
    '''Execution routine for ring_buffer'''
    return x * 2

