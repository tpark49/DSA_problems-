def findDuplicates(nums):
    for e in nums:
            if nums[abs(e)] < 0:
                return abs(e)
            nums[abs(e)] = -nums[abs(e)]

def solution2(nums):
    fast = 0 
    slow = 0 

    while True: 
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast: 
            break
    
    slow2 = 0 

    while True: 
        slow = nums[slow]
        slow2 = nums[slow2]

        if slow == slow2: 
            return slow 


    
if __name__ == "__main__":
    print(findDuplicates([1,3,4,2,3]))