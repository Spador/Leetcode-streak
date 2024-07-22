class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        # Initialize frequency maps for all lowercase letters
        map1 = {chr(ord('a') + i): 0 for i in range(26)}
        map2 = {chr(ord('a') + i): 0 for i in range(26)}

        # Count frequencies of characters in s1
        for c in s1:
            map1[c] += 1

        # Build the initial window (length = len(s1)) in s2
        for i in range(len(s1)):
            map2[s2[i]] += 1

        # Count how many letters currently match in frequency
        matches = 0
        for ch in map1:
            if map1[ch] == map2[ch]:
                matches += 1

        left = 0
        right = len(s1) - 1

        # Slide the window over s2
        while right < len(s2) - 1:
            if matches == 26:
                return True

            # Expand window by moving right pointer
            right += 1
            c = s2[right]
            # If this letter was previously matching, we'll lose a match
            if map1[c] == map2[c]:
                matches -= 1
            map2[c] += 1
            # If this letter now matches, increment matches
            if map1[c] == map2[c]:
                matches += 1

            # Shrink window by moving left pointer
            d = s2[left]
            if map1[d] == map2[d]:
                matches -= 1
            map2[d] -= 1
            if map1[d] == map2[d]:
                matches += 1

            left += 1

        # Check the last window
        return matches == 26
