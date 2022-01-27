def missingElement(nums, k):
    if not nums or k == 0: 
        return 0 

    number_gap = nums[-1] - nums[0] + 1 
    missing = number_gap - len(nums)

    if missing < k: 
        return nums[-1] + k - missing 

    
    l = 0 
    r = len(nums)-1 

    while l<r: 
        mid = (l+r)//2

        number_gap = nums[mid] - nums[l] + 1
        missing = number_gap - len(nums[:mid+1])

        if missing < k: 
            l= mid 
            k -= missing 
        else: 
            r = mid

    return nums[l]


