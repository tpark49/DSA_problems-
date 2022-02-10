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
    
if __name__ == "__main__":
    print(minSubArrayLen(7,[2,3,1,2,4,3]))
