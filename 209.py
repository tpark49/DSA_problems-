#O(N) solution
def minSubArrayLen(target, nums):
    l, r, total = 0, 0, 0 

    result = float("inf")

    
    while r<len(nums):
        total += nums[r]

        while total >= target: 
            result = min(result, r-l+1)
            total -= nums[l]
            l+=1
        r+=1

    if result == float("inf"):return 0 
    else: return result

#O(Nlog(N))
def secondSolution(target, nums):
    #cumulative sum 
    summed = [0 for i in nums]
    summed[0] = nums[0]
    for i in range(1, len(nums)):
        summed[i] = summed[i-1] + nums[i]
     
    def binary_search(l, summed, target): 
        r = len(summed)-1
        if l == 0: 
            offset = 0 
        else: 
            offset = summed[l-1]
        
        while l<=r: 
            mid = (l+r)//2
            if summed[mid]-offset>=target: 
                r = mid -1 
            else: 
                l = mid + 1
        return l 

    result = float("inf")
    for l in range(len(nums)):
        r = binary_search(l, summed, target)
        if r == len(nums):
            break
        result = min(result, r - l + 1)

    if result == float("inf"):return 0 
    else: return result

if __name__ == "__main__":
    print(secondSolution(11,[1,1,1,1,1,1,1,1]))
