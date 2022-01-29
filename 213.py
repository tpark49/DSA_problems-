def rob(nums):
    prev2, prev, cur = 0 ,0, 0

    for i in range(len(nums)): 
        cur = max(prev2 + nums[i], prev)

        prev2 = prev

        prev = cur 

    return cur

def helper(nums):
    if len(nums)<=1: 
        return nums[0]

    return max(rob(nums[:len(nums)-1]), rob(nums[1:]))




if __name__ == "__main__":
    print(helper([1]))