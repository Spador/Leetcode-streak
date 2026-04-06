# spador

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        env = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        dp = []

        for wid, hei in env:
            # i = bisect_left(dp, hei)

            left, right = 0, len(dp) - 1
            i = left
            while left <= right:
                mid = (left + right)//2
                if hei > dp[mid]:
                    left = mid + 1
                elif hei < dp[mid] :
                    right = mid - 1
                else:
                    left = mid
                    break
            i = left

            if i == len(dp):
                dp.append(hei)
            else:
                dp[i] = hei

        return len(dp)
