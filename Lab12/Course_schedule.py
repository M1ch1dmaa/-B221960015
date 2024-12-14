from collections import defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        # Create a graph as an adjacency list
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        # State: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def has_cycle(course):
            if state[course] == 1:  # If visiting, cycle detected
                return True
            if state[course] == 2:  # If already visited, no cycle
                return False
            
            # Mark as visiting
            state[course] = 1
            for neighbor in graph[course]:
                if has_cycle(neighbor):
                    return True
            
            # Mark as visited
            state[course] = 2
            return False

        # Check all courses for cycles
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True
