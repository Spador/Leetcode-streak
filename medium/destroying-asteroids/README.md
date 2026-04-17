# Destroying Asteroids

Given a planet with initial mass and a list of asteroids, determine if the planet can destroy all asteroids. The planet can destroy an asteroid if its mass >= asteroid's mass, and it absorbs that mass afterward.

## Approach
- Sort asteroids in ascending order
- Greedily absorb each asteroid if current mass allows it; otherwise return False
- Return True if all asteroids are destroyed

Time Complexity: O(n log n)
Space Complexity: O(1)
