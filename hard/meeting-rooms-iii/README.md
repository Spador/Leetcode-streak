# Meeting Rooms III

Return the room number that held the most meetings; break ties by lowest room number.

## Approach
- Sort meetings by start time
- Use a min-heap for free rooms (by room number) and a min-heap for busy rooms (by end time, then room number)
- For each meeting: free up any rooms whose end time <= current start time
- If no free room, pop the earliest-ending busy room and adjust the meeting's end time by the delay
- Assign the lowest-numbered free room, push it to the busy heap, and increment its booking count
- Return the index of the maximum in the booking count array

Time Complexity: O(m log n) where m is number of meetings
Space Complexity: O(n)
