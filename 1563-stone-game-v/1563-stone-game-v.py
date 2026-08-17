class Solution(object):
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + stoneValue[i]
        res = [[-1] * n for _ in range(n)]

        return self.solve(0, n - 1, prefix_sum, res)
    def solve(self, l, r, prefix_sum, res):
        if l >= r:
            return 0
        if res[l][r] != -1:
            return res[l][r]
        ans = 0
        left_sum = 0
        total = prefix_sum[r + 1] - prefix_sum[l]
        for mid in range(l, r):
            left_sum += prefix_sum[mid + 1] - prefix_sum[mid]
            right_sum = total - left_sum
            if left_sum < right_sum:

                # Pruning
                if ans >= left_sum * 2:
                    continue
                ans = max(
                    ans,
                    left_sum + self.solve(l, mid, prefix_sum, res)
                )
            elif left_sum > right_sum:

                # Pruning
                if ans >= right_sum * 2:
                    break

                ans = max(
                    ans,
                    right_sum + self.solve(mid + 1, r, prefix_sum, res)
                )

            # Equal
            else:
                ans = max(
                    ans,
                    left_sum + self.solve(l, mid, prefix_sum, res),
                    right_sum + self.solve(mid + 1, r, prefix_sum, res)
                )

        res[l][r] = ans
        return ans