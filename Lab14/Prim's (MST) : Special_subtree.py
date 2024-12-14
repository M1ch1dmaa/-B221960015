import heapq
import sys

def prims(n, edges, start):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, w in edges:
        graph[u].append((w, v))
        graph[v].append((w, u))
    
    pq = []
    visited = set()
    mst_weight = 0
    
    heapq.heappush(pq, (0, start))
    
    while pq:
        weight, node = heapq.heappop(pq)
        
        if node in visited:
            continue
        
        mst_weight += weight
        visited.add(node)
        
        for next_weight, neighbor in graph[node]:
            if neighbor not in visited:
                heapq.heappush(pq, (next_weight, neighbor))
    
    return mst_weight

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().splitlines()
    
    n, m = map(int, data[0].split())
    edges = []
    for i in range(1, m + 1):
        u, v, w = map(int, data[i].split())
        edges.append((u, v, w))
    start = int(data[m + 1])
    
    result = prims(n, edges, start)
    print(result)

