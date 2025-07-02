def longest_increasing_subsequence(arr):
    if not arr:
        return 0

    n = len(arr)
    dp = [1] * n  # dp[i] stores the length of LIS ending at index i

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print("Length of Longest Increasing Subsequence:", longest_increasing_subsequence(nums))
