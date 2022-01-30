def uniquePaths(m, n):

    result = [[1 for i in range(n)] for j in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            result[i][j] = result[i-1][j] + result[i][j-1]

    return result[-1][-1]

if __name__ == "__main__":
    print(uniquePaths(3,7))