def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    size1 = len(text1)
    size2 = len(text2)
    dp = [[0 for col in range(size2 + 1)] for row in range(size1 + 1)]
    dp[0][0] = 0

    for i in range(1, size1 + 1):
        dp[i][1] = 1 if text1[i - 1] == text2[0] else dp[i - 1][1]

    for j in range(1, size2 + 1):
        dp[1][j] = 1 if text2[j - 1] == text1[0] else dp[1][j - 1]

    for i in range(1, size1 + 1):
        for j in range(1, size2 + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[size1][size2]