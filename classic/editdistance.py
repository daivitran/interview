def lengthOfLIS(self, nums) -> int:
    result = 0
    dp = [1 for _ in nums]

    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
        result = max(result, dp[i])

    return result