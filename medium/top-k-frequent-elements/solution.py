from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #First make a dictionary to store the count(occurance) of each number
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        
        #Then use the logic for bucket sort by modifying it. Each index i of the bucket list signifies the number of time an element has occured and at that i position it stores the list of element that has occured i times.
        bucket = [[] for i in range(len(nums)+1)]
        for n,c in count.items():
            bucket[c].append(n)

        #Finally, iterate in the bucket from the back of the list and add top k elements to the result list.
        result = []

        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                result.append(n)
                if len(result) == k:
                    return result 