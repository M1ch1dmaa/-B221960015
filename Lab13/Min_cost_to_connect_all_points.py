import heapq

class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        visited = set()
        min_heap = [(0, 0)]  # (cost, point_index)
        total_cost = 0

        while len(visited) < n:
            cost, curr = heapq.heappop(min_heap)

            if curr in visited:
                continue

            visited.add(curr)
            total_cost += cost

            for next_point in range(n):
                if next_point not in visited:
                    next_cost = abs(points[curr][0] - points[next_point][0]) + abs(points[curr][1] - points[next_point][1])
                    heapq.heappush(min_heap, (next_cost, next_point))

        return total_cost
