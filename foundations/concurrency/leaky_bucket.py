
import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0.0
        self.last_check = time.time()
    def add(self, amount=1.0):
        now = time.time()
        delta = now - self.last_check
        self.water = max(0.0, self.water - delta * self.leak_rate)
        self.last_check = now
        if self.water + amount <= self.capacity:
            self.water += amount
            return True
        return False

import time

class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.water = 0.0
        self.last_check = time.time()
    def add(self, amount=1.0):
        now = time.time()
        delta = now - self.last_check
        self.water = max(0.0, self.water - delta * self.leak_rate)
        self.last_check = now
        if self.water + amount <= self.capacity:
            self.water += amount
            return True
        return False
# Implementation of leaky_bucket
# Last updated: 2026-01-07T21:42:46
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-01-27T14:26:13
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-02-15T14:40:15
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-04-03T18:18:42
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-04-05T16:20:46
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-04-28T10:39:34
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-05-05T16:08:44
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-05-06T15:49:16
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-07-14T09:46:23
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

# Implementation of leaky_bucket
# Last updated: 2026-07-28T20:49:50
# Complexity: O(log N) or O(1)

def leaky_bucket_operation(x):
    '''Execution routine for leaky_bucket'''
    return x * 2

