# Meeting Rooms

Given an array of meeting time intervals, determine if a person could attend all meetings.

## Approach
- Sort intervals by start time
- Iterate through consecutive pairs; if the next meeting starts before the previous one ends, return False
- Return True if no overlaps found

Time Complexity: O(n log n)
Space Complexity: O(1)
