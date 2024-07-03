# Two Sum

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

## Approach
- Use a hashmap to store complements (target - current number)
- For each number, check if it exists in hashmap
- If found, return current index and stored index
- If not found, store complement with current index

Time Complexity: O(n)
Space Complexity: O(n)

### Examples:
```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [3,2,4], target = 6
Output: [1,2]

Input: nums = [3,3], target = 6
Output: [0,1]
```

### Constraints:
- 2 <= nums.length <= 104
- -109 <= nums[i] <= 109
- -109 <= target <= 109
- Only one valid answer exists

### Example Walkthrough:
For nums = [2,7,11,15] and target = 9:

1. First iteration (i=0, num=2):
   - Check if 2 exists in hashmap (it doesn't)
   - Store complement (9-2=7) in hashmap: {7: 0}

2. Second iteration (i=1, num=7):
   - Check if 7 exists in hashmap (it does!)
   - Return [hashmap[7], 1] = [0, 1]

This approach is more efficient than the brute force O(n²) solution as we only need to traverse the array once. 