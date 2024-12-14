class Solution:
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        reach = [[False] * numCourses for _ in range(numCourses)]
        
        for pre, course in prerequisites:
            reach[pre][course] = True
        
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
        
        return [reach[u][v] for u, v in queries]
