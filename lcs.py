def lcs_recursive(s1, s2):
    def dp(i, j):
        if i == -1 or j == -1:
            return 0
        if s1[i] == s2[j]:
            return dp(i-1, j-1) + 1
        else:
            return max(dp(i-1, j), dp(i, j-1))

    return dp(len(s1) - 1, len(s2) - 1)


def lcs_dp(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # return dp[-1][-1]

    # Print lcs
    longest = dp[-1][-1]
    s = [''] * longest
    idx = -1
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            i -= 1
            j -= 1
            s[idx] = s1[i]
            idx -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(s)


if __name__ == "__main__":
    print(lcs_recursive('babcde', 'acze'))
    print(lcs_dp('babcde', 'acze'))
