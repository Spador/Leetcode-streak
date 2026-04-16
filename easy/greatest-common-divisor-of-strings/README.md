# Greatest Common Divisor of Strings

Return the largest string that divides both str1 and str2 (divides = can be repeated to form the string).

## Approach
- If str1 + str2 != str2 + str1, no common divisor exists; return ""
- Otherwise the GCD string has length equal to GCD of the two string lengths (Euclidean algorithm)
- Return str1[:gcd_length]

Time Complexity: O(m + n)
Space Complexity: O(m + n)
