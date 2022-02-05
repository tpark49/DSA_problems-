def findPeakElement(nums):

    if nums[0]>nums[1]:
        return 0

    if nums[-1]>nums[-2]:
        return len(nums)-1

    left = 1
    right = len(nums)-2

    while left<=right: 
        mid = (left+ right)//2

        if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
            return mid

        elif nums[mid-1]>nums[mid]:
            right = mid - 1 
        
        else: 
            left =  mid + 1

    
if __name__ == "__main__":
    print(findPeakElement([1,2,1,3,5,6,4]))
