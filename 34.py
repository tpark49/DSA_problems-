def searchRange(nums, target):
    
    def find_first(nums, target):
        l = 0
        r = len(nums)-1
        res = -1
        while l<=r: 
            mid = (l+r)//2
            if nums[mid] == target:
                res = mid 
                r = mid - 1
            elif nums[mid] > target: 
                r = mid - 1
            else: 
                l = mid + 1     
        return res

    def find_last(nums,target):
        res = -1 
        l = 0
        r = len(nums)-1
        while l<=r: 
            mid = (l+r)//2
            if nums[mid] == target: 
                res = mid 
                l = mid + 1
            elif nums[mid] > target: 
                r = mid - 1
            else: 
                l = mid + 1 
        return res 

    first_index = find_first(nums, target)
    last_index = find_last(nums, target)

    return [first_index, last_index]

if __name__ == "__main__":
    print(searchRange([5,7,7,8,8,10], 6))