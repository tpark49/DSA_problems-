def canJump(nums):
    result = [False for i in nums]
    result[-1] = True
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] + 1 < len(nums):
            result[i] = any(result[i:i+nums[i]+1])

        else: 
            result[i] = any(result[i:])

    return result[0]
        
if __name__ == "__main__":
    print(canJump([3,2,1,0,4]))
