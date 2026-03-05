# spador

# sliding window approach

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        fcount = defaultdict(int)
        left, total, result = 0, 0, 0

        for right in range(len(fruits)):
            fcount[fruits[right]] += 1
            total += 1

            while len(fcount) > 2:
                f = fruits[left]
                fcount[f] -= 1
                total -= 1
                left += 1
                if not fcount[f]:
                    fcount.pop(f)
            result = max(result, total)
        return result
