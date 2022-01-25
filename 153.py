import random
def findMin(nums):

    l = 0 
    r = len(nums)-1

    while l<r: 
        mid = (l + r)//2

        if nums[r]>num[mid]:
            r = mid
        else: 
            l = mid + 1

    return nums[r]

