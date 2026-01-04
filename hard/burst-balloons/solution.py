# spador

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # recursive solution 2D dp
        # Time: O(n^2 * n)
        # Space: O(n^2)
        # l, r = left pointer, right pointer
        # we are recursively calculating which baloon pops last to make it easier to break into sub problems instead
        # of checking which burst first because we won't be able to break into sub problems then
        nums = [1] + nums + [1]
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        return dfs(1, len(nums) - 2)


