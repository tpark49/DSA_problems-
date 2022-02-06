def findPeakGrid(mat):
    
    for row in range(len(mat)): 
        if row == 0:
            if mat[row][0]>mat[row][1] and mat[row][0] > mat[row+1][0]:
                return [row, 0]

            if mat[row][-1]>mat[row][-2] and mat[row][-1] > mat[row+1][-1]:
                return [row, len(mat[0])-1]
        
        if row == len(mat)-1:
            if mat[row][0]>mat[row][1] and mat[row][0] > mat[row-1][0]:
                return [row, 0]

            if mat[row][-1]>mat[row][-2] and mat[row][-1] > mat[row-1][-1]:
                return [row, len(mat[0])-1]

        l = 1 
        r = len(mat[0])-2

        while l <= r: 
            mid = (l+r)//2

            if row == 0:
                if mat[row][mid]>mat[row][mid-1] and mat[row][mid]>mat[row][mid+1] and mat[row][mid]> mat[row+1][mid]:
                    return [row, mid]
            elif row == len(mat)-1:
                if mat[row][mid]>mat[row][mid-1] and mat[row][mid]>mat[row][mid+1] and mat[row][mid] > mat[row-1][mid]:
                    return [row, mid]
            else: 
                if mat[row][mid]>mat[row][mid-1] and mat[row][mid]>mat[row][mid+1] and mat[row][mid]>mat[row+1][mid] and mat[row][mid]>mat[row-1][mid]:
                    return [row, mid]

            if mat[row][mid+1] > mat[row][mid]:
                l = mid + 1
            
            else: 
                r = mid - 1

if __name__ == "__main__":
    print(findPeakGrid([
        [10,50,40,30,20],
        [1,500,2,3,4]]))



        
