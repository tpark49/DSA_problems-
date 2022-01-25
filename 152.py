def maxProduct(array):
    res = array[0]
    cur_min, cur_max = 1, 1

    for num in array: 
        val = [num, num*cur_min, num*cur_max]

        cur_min = min(val)
        cur_max = max(val)

        res = max(res, cur_max)

    return res

if __name__ == "__main__":
    print(maxProduct([-2,0,-1]))