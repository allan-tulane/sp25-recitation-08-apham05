from collections import deque
from heapq import heappush, heappop 

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    ### TODO

    heap = []  
    heappush(heap, (0, 0, source))  
    best = {} 
  
    while heap:
        dist, edges, u = heappop(heap)
        if u in best:
            continue
        best[u] = (dist, edges)
        for v, w in graph.get(u, set()):
            if v not in best:
                new_dist = dist + (int(w) if isinstance(w, str) else w)
                heappush(heap, (new_dist, edges + 1, v))
    return best
    #pass
    

    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    ###TODO
    parents = {source: None}
    visited = {source}
    queue = deque([source])

    while queue:
        u = queue.popleft()
        for v in graph.get(u, set()):
            if v not in visited:
                visited.add(v)
                parents[v] = u
                queue.append(v)
    return parents


    pass

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }


    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    ###TODO
    path = []
    while destination in parents and parents[destination] is not None:
        path.append(parents[destination])
        destination = parents[destination]
    return ''.join(path[::-1])
    pass

