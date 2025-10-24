from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list - each course maps to its prerequisites
        prereqMap = {c: [] for c in range(numCourses)}
        
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)
        
        # Track courses in different states
        result = []  # Final topological ordering
        visited = set()  # Courses completely processed
        currentLoop = set()  # Courses currently being processed (for cycle detection)
        
        def dfs(course):
            # If we encounter a course we're currently processing, we have a cycle
            if course in currentLoop:
                return False
            
            # If course is already processed, skip it
            if course in visited:
                return True
            
            # Mark course as currently being processed
            currentLoop.add(course)
            
            # Process all prerequisites first
            for prereq in prereqMap[course]:
                if dfs(prereq) == False:
                    return False
            
            # Add course to result after processing all prerequisites (post-order)
            result.append(course)
            visited.add(course)
            currentLoop.remove(course)
            return True
        
        # Check all courses
        for course in range(numCourses):
            if dfs(course) == False:
                return []  # Cycle detected, return empty array
        
        return result
