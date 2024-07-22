##spador

class TimeMap:

    def __init__(self):
        self.hashmap = {} #key(str): list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value = self.hashmap.get(key, [])

        left = 0
        right = len(value) - 1
        while left <= right:
            middle = (left + right) // 2

            if value[middle][1] == timestamp:
                return value[middle][0]
            elif value[middle][1] < timestamp:
                result = value[middle][0]
                left = middle + 1
            else:
                right = middle - 1
        
        return result
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
