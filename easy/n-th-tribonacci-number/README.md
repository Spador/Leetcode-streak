# N-th Tribonacci Number

Return the n-th Tribonacci number where T0=0, T1=1, T2=1, and Tn+3 = Tn + Tn+1 + Tn+2.

## Approach
- Handle base cases n=0, 1, 2 directly
- Use three variables to track the last three values, rolling them forward each iteration
- Run n-2 iterations to reach the n-th value

Time Complexity: O(n)
Space Complexity: O(1)
