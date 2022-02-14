def singleNonDuplicates(nums):

    l = 0
    r = len(nums)-1

    while l < r: 
        mid = int((l + r)/2)
        if (mid %2 == 0 and nums[mid]==nums[mid+1]) or (mid %2 ==1 and nums[mid] == nums[mid-1]):
            l = mid + 1

        else: 
            r = mid 
        
    return nums[l] 

if __name__ == "__main__":
    print(singleNonDuplicates([1,1, 2,2,3,3,4,4,8]))


        

