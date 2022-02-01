def findMaxConsecutiveOnes(nums):

    result = 0 
    count = 0 
    for i in nums: 
        if i == 1:
            count +=1 
            result = max(result, count)
        else: 
            count = 0 

    return result

if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1,0,1,1,0,1]))

