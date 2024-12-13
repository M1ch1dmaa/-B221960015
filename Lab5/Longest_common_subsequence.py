class Solution:
    def longestCommonSubsequence(self, text1, text2):
        text1_length = len(text1)
        text2_length = len(text2)

        # Initialize the DP table with zeros
        dp = [[0] * (text2_length + 1) for _ in range(text1_length + 1)]

        for i in range(1, text1_length + 1):
            for j in range(1, text2_length + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[text1_length][text2_length]
