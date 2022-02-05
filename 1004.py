def longestOne(nums, k):
    number_zeros = 0 
    start = 0 
    res = 0 

    for i, end in enumerate(nums):
        
        if end == 0: 
            number_zeros +=1

        while number_zeros>k: 
            if nums[start] == 0: 
                number_zeros -=1
            start +=1

        res = max(res, i - start + 1)
    
    return res

if __name__ == "__main__":
    print(longestOne([1,1,1,0,0,0,1,1,1,1,0], 2))