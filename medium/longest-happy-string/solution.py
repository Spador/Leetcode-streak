import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ""
        maxHeap = []
        
        # Build max heap using negative values (min heap with negatives = max heap)
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            
            # If last two characters are the same, use second character instead
            if len(result) > 1 and result[-1] == result[-2] == char:
                if not maxHeap:
                    # Can't add more characters, break
                    break
                
                # Use second most frequent character
                count2, char2 = heapq.heappop(maxHeap)
                result += char2
                count2 += 1  # Decrement count (negative value, so +1)
                
                if count2:  # If count2 < 0 (still has characters)
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                # Add current character
                result += char
                count += 1  # Decrement count (negative value, so +1)
            
            # Push character back to heap if it still has count remaining
            if count:  # If count < 0 (still has characters)
                heapq.heappush(maxHeap, (count, char))
        
        return result
