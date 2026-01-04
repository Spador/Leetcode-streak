# spador

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr.sort()
        currMin = arr[-1] - arr[0]
        for i in range(len(arr)-1):
            currMin = min(currMin, arr[i+1] - arr[i])
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] == currMin:
                result.append([arr[i], arr[i+1]])
        return result



