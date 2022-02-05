def findMaxConsecutiveOnes(nums):
    start = 0
    max_zeros = 1
    num_zeros = 0

    for i, end in enumerate(nums):

        if i == 0 : 
            num_zeros +=1 

        while num_zeros > max_zeros:

            if nums[start] == 0: 
                num_zeros -=1

            start +=1 

        result = max(result, end - start + 1) 

    return result 


def secondSolution(nums):
    prev, curr = 0, 0 
    res = 0 

    for i in nums: 
        if i == 0: 
            prev, curr = curr, 0 
        
        else: 
            curr +=1 

        result = max(result, prev + 1 + curr)

    return result



if __name__ == "__main__":
    print(findMaxConsecutiveOnes([1,0,0,1,1,1,1,1,1]))
                