def canJump(nums):
    result = [False for i in nums]
    result[-1] = True
    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] + 1 < len(nums):
            result[i] = any(result[i:i+nums[i]+1])

        else: 
            result[i] = any(result[i:])

    return result[0]

def canJump2(nums):
    goal = len(nums)- 1

    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal: 
            goal = i
        
    return goal == 0 
        
if __name__ == "__main__":
    print(canJump2([2,3,1,1,4]))
