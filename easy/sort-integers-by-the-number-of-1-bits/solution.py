# spador

class Solution:

    def setBit(self, num: int) -> int:
        bits = 0
        while num:
            bits += num & 1
            num >>= 1
        return bits

    def sortByBits(self, arr: List[int]) -> List[int]:
        bitCount = [0] * len(arr)
        for i in range(len(arr)):
            bitCount[i] = self.setBit(arr[i])

        result, bitDict = [], defaultdict(list)

        for i in range(len(arr)):
            heapq.heappush(bitDict[bitCount[i]], arr[i])

        for key in sorted(bitDict):
            while bitDict[key]:
                result.append(heapq.heappop(bitDict[key]))

        return result
