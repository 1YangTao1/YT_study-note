#动态规划
class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n = len(nums)
        maxnums = max(nums)
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ // 2
        if maxnums > target:
            return False
        dp = [[False] * (target + 1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True

        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
                if j == target:
                    if dp[i][j] == True:
                        break
        return dp[i][target]

#动态规划优化
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        maxnums = max(nums)
        sum_ = sum(nums)
        if sum_ % 2 == 1:
            return False

        target = sum_ // 2
        if maxnums > target:
            return False
        dp = [True] + [False] * target

        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                if dp[target]:
                    return True
                dp[j] = dp[j] | dp[j - num]
        return dp[target]