# 636. Exclusive Time of Functions

**Difficulty:** Medium

## Problem Description
On a single-threaded CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n - 1`.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list `logs`, where `logs[i]` represents the `i`th log message formatted as a string `"{function_id}:{'start' | 'end'}:{timestamp}"`.

Return the exclusive time of each function in an array, where the value at the `i`th index represents the exclusive time for the function with ID `i`.

## Examples

### Example 1
```
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
```

### Example 2
```
Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
```

### Example 3
```
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: [7,1]
```

## Constraints
- `1 <= n <= 100`
- `2 <= logs.length <= 500`
- `0 <= function_id < n`
- `0 <= timestamp <= 10^9`
- No two start events will happen at the same timestamp.
- No two end events will happen at the same timestamp.
- Each function has an `"end"` log for each `"start"` log.

## Approach
Because the CPU is single-threaded, only the function at the **top of the stack** is executing at any given moment.

We can simulate the call stack and track exclusive execution time:

1. Maintain:
   - `execTime`: an array of length `n` where `execTime[i]` is the total exclusive time for function `i`.
   - `stack`: a call stack that stores the IDs of currently running functions.
   - `prevStart`: the timestamp where the current top-of-stack function started (or resumed) executing.
2. For each log string `s` in `logs`:
   - Parse it into `pid`, `action`, and `currTime`.
   - If `action == "start"`:
     - If there is a function already running on top of the stack, we add the time from `prevStart` up to `currTime` to that function’s exclusive time:
       - `execTime[stack[-1]] += currTime - prevStart`.
     - Push the new `pid` onto the stack and set `prevStart = currTime`.
   - If `action == "end"`:
     - The function on top of the stack ends at `currTime` **inclusive**, so we add `currTime - prevStart + 1` to its exclusive time:
       - `execTime[stack.pop()] += currTime - prevStart + 1`.
     - Then set `prevStart = currTime + 1`, as the next function (if any) resumes at the next timestamp.
3. After processing all logs, return `execTime`.

This correctly attributes time to each function, subtracting out time spent in nested calls.

## Time & Space Complexity
- **Time Complexity:** `O(L)`, where `L = len(logs)`, since we process each log once.
- **Space Complexity:** `O(n)` for the `execTime` array and up to `O(n)` for the stack in the worst case (deep recursion).

