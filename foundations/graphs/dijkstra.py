
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

