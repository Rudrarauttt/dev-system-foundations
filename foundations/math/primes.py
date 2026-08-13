
def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [i for i, is_p in enumerate(primes) if is_p]

def is_prime(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if primes[p]:
            for i in range(p * p, limit + 1, p):
                primes[i] = False
    return [i for i, is_p in enumerate(primes) if is_p]
# Implementation of primes
# Last updated: 2026-01-12T17:47:21
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-02-05T12:17:17
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-02-07T15:45:47
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-02-27T16:20:37
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-03-12T16:49:37
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-03-30T19:27:20
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-04-09T19:22:41
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-06-01T15:29:28
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-06-01T17:35:39
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-06-17T15:11:11
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-07-02T11:31:30
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

# Implementation of primes
# Last updated: 2026-08-13T14:22:14
# Complexity: O(log N) or O(1)

def primes_operation(x):
    '''Execution routine for primes'''
    return x * 2

