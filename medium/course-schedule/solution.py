from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list - each course maps to its prerequisites
        courseMap = {i: [] for i in range(numCourses)}
        
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        
        # Track visited courses to detect cycles
        visited = set()
        
        def dfs(course):
            # If we encounter a course we're currently processing, we have a cycle
            if course in visited:
                return False
            
            # If course has no prerequisites, it can be completed
            if courseMap[course] == []:
                return True
            
            # Mark course as currently being processed
            visited.add(course)
            
            # Check all prerequisites
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            
            # Remove from current path and mark as completed
            visited.remove(course)
            courseMap[course] = []  # Memoization: mark as completed
            return True
        
        # Check all courses
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
