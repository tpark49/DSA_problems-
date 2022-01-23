def maxSubarray(nums):
    dp = [None for i in nums]
    dp[0] = nums[0]
    result = nums[0]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i], nums[i] + dp[i-1])
        result = max(result, dp[i])

    return result 


if __name__ == "__main__":
    print(maxSubarray([1]))




    