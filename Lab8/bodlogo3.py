import heapq

def assign_bikes(students, bikes):
    n = len(students)
    m = len(bikes)
    
    distance_heap = []
    for i, student in enumerate(students):
        for j, bike in enumerate(bikes):
            dist = abs(student[0] - bike[0]) + abs(student[1] - bike[1])
            heapq.heappush(distance_heap, (dist, i, j))
    
    assigned_bikes = [-1] * n
    used_bikes = set()
    
    while len(used_bikes) < n:
        dist, student_idx, bike_idx = heapq.heappop(distance_heap)
        if assigned_bikes[student_idx] == -1 and bike_idx not in used_bikes:
            assigned_bikes[student_idx] = bike_idx
            used_bikes.add(bike_idx)
    
    return assigned_bikes

import unittest

class TestAssignBikes(unittest.TestCase):
    def test_case_1(self):
        students = [(0, 0), (1, 1)]
        bikes = [(0, 1), (4, 3), (2, 1)]
        expected = [0, 2]
        self.assertEqual(assign_bikes(students, bikes), expected)

if __name__ == "__main__":
    unittest.main()
