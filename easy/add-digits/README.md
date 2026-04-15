# Add Digits

Repeatedly sum all digits of a number until a single digit remains; return that digit.

## Approach
- Based on the digital root property: a number's repeated digit sum equals its value mod 9
- Special cases: 0 returns 0; multiples of 9 return 9; all others return num % 9

Time Complexity: O(1)
Space Complexity: O(1)
