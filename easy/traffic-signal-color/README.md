# Traffic Signal Color

Return the traffic signal state based on the remaining timer value.

## Approach
- Directly map timer values to states: 0 → Green, 30 → Orange, (30, 90] → Red, otherwise → Invalid

Time Complexity: O(1)
Space Complexity: O(1)
