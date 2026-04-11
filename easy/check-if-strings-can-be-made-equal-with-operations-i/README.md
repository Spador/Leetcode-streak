# Check if Strings Can be Made Equal With Operations I

Given two length-4 strings, determine if they can be made equal by swapping characters at indices i and j where j - i = 2.

## Approach
- Walk both strings character by character with two pointers
- If characters differ, try swapping s1[p1] with s1[p1+2] (the only valid swap for that position)
- If the swap fixes the mismatch, apply it; otherwise return False

Time Complexity: O(1)
Space Complexity: O(1)
