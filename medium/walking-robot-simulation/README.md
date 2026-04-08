# Walking Robot Simulation

Simulate a robot on an infinite XY-plane following commands with obstacles, and return the maximum squared Euclidean distance reached.

## Approach
- Store obstacles in a set of tuples for O(1) lookup
- Maintain a direction array [N, E, S, W] and a direction index; rotate by +1 (right) or -1 (left) mod 4
- For move commands step one unit at a time, stopping if the next cell is an obstacle
- Track the maximum x² + y² after each step

Time Complexity: O(n * k) where n is commands length and k is max move distance (9)
Space Complexity: O(m) where m is number of obstacles
