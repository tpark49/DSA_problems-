def rob(num):

    result = [0 for i in range(len(num))]
    result[0] = num[0]
    result[1] = max(num[0], num[1])
    for i in range(2, len(num)): 
        result[i] = max(result[i-1],result[i-2] + num[i])

    return max(result)


def rob2(num):
    prev2, prev, cur = 0 , 0 , 0 

    for i in num: 
        cur = max(prev2 + i, prev)
        prev2 = prev 
        prev = cur 

    return cur 


if __name__ == "__main__":
    print(rob2([2,7,9,3,1]))