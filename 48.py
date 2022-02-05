def rotate(matrix):
    #reverse 

    #this operation is not in place you are making a new copy 
    # matrix = matrix[::-1]

    l = 0 
    r = len(matrix)-1
    while l < r :
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l+=1
        r-=1

    for row in range(len(matrix)):
        for col in range(row, len(matrix[0])):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
    
    return matrix 


if __name__ == "__main__":
    print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
