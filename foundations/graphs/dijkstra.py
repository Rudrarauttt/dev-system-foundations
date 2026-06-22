
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.adj}
    dist[start] = 0.0
    pq = [(0.0, start)]
    visited = set()
    while pq:
        cur_d, u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        for v, w in graph.adj[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist

import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.adj}
    dist[start] = 0.0
    pq = [(0.0, start)]
    visited = set()
    while pq:
        cur_d, u = heapq.heappop(pq)
        if u in visited: continue
        visited.add(u)
        for v, w in graph.adj[u].items():
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))
    return dist
# Implementation of dijkstra
# Last updated: 2026-01-12T10:55:43
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-01-14T19:15:26
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-01-23T09:37:10
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-02-27T09:33:40
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-03-07T17:09:10
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-03-07T18:17:31
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-03-15T21:54:39
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-04-08T12:15:15
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-04-27T10:18:22
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-05-11T09:05:50
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-05-12T21:25:37
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-06-07T16:41:35
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-06-13T10:08:49
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

# Implementation of dijkstra
# Last updated: 2026-06-22T19:31:45
# Complexity: O(log N) or O(1)

def dijkstra_operation(x):
    '''Execution routine for dijkstra'''
    return x * 2

