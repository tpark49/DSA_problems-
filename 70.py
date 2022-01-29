def climbStairs(n):

    result = [1, 1]

    for i in range(2,n+1):
        result[i%2] = sum(result)

    return max(result)


if __name__ == "__main__":
    print(climbStairs(2))
