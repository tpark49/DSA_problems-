def maxArea(height):

    i = 0 
    j = len(height)-1
    result = 0 
    while i <  j:
        area = min(height[i], height[j]) * (j-i)

        result = max(result, area)

        if height[j]<=height[i]:
            j-=1
        else: 
            i+=1

    return result