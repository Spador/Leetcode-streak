# spador

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 0: return ""
        
        # countT dict holds count of each char in t
        # window dict will hold count of char in current window
        countT, window = {}, {}
        
        # iterating through t to fill countT
        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)
        
        # need: count of what is required , have: current count of what is fullfilled
        need, have = len(countT), 0           

        left = 0
        result = [-1, -1]
        resLen = float("infinity")   # result has pointers left & right

        for right in range(len(s)):
            # add character to the window
            ch = s[right]
            window[ch] = 1 + window.get(ch, 0)
            
            if ch in countT and countT[ch] == window[ch]:
                have += 1
            
            # if have and need are equal then we update result and increment left till
            # we find a better solution
            while have == need:
                # update the result
                if (right - left + 1) < resLen:
                    result = [left, right]
                    resLen = (right -  left + 1)
                
                # popping from the left of the window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        left, right = result
        return s[left:right + 1] if resLen != float("infinity") else ""
