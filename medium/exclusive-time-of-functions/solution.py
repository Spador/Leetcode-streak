# spador

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # there is only single threaded CPU, it can only complete the 
        # process at the top of the stack.
        
        execTime = [0] * n  # execution time for each process
        stack = []          # call stack
        prevStart = 0       # previous start time stamp

        for s in logs:
            pid, action, time = s.split(":")
            pid = int(pid)
            currTime = int(time)

            if action == "start":
                if stack:
                    execTime[stack[-1]] += currTime - prevStart
                stack.append(pid)
                prevStart = currTime
            else:
                execTime[stack.pop()] += currTime - prevStart + 1
                prevStart = currTime + 1           
                
        return execTime


