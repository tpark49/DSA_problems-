def uniquePathsWithObstacles(obstacleGrid): 

    col_flagged = False
    row_flagged = False
    if obstacleGrid[0][0] == 1: 
        col_flagged = True 
        row_flagged = True 
        obstacleGrid[0][0] = 0 
    else:
        obstacleGrid[0][0] = 1
 
    #change first col 
    for col in range(1, len(obstacleGrid[0])):
        if col_flagged: 
            obstacleGrid[0][col] = 0 
        else: 
            if obstacleGrid[0][col] == 1: 
                obstacleGrid[0][col] = 0 
                col_flagged = True 
            else: 
                obstacleGrid[0][col] = 1 

    for row in range(1, len(obstacleGrid)):
        if row_flagged: 
            obstacleGrid[row][0] = 0
        else:        
            if obstacleGrid[row][0] ==1: 
                obstacleGrid[row][0] = 0
                row_flagged = True
            else: 
                obstacleGrid[row][0] = 1     

    for i in range(1, len(obstacleGrid)):
        for j in range(1, len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1:
                obstacleGrid[i][j] = 0 
            else: 
                obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

    return obstacleGrid


if __name__ == "__main__":
    print(uniquePathsWithObstacles([[0]]))
                 