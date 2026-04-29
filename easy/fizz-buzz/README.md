# 412. Fizz Buzz

Return a string array where each element is "Fizz", "Buzz", "FizzBuzz", or the number itself based on divisibility rules.

## Approach
- Iterate from 1 to n, checking divisibility by 3 and 5 using boolean flags
- Append "FizzBuzz" if both flags are true, "Fizz" if only divisible by 3, "Buzz" if only divisible by 5, else the number as a string

Time Complexity: O(n)
Space Complexity: O(n)
