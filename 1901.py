def findPeakGrid(mat):

    start = 0 
    end = len(mat[0])-1

    while start <= end:

        mid = (start + end)//2

        largest_i, res = 0, float("-inf")
        for i in range(len(mat)):
            if mat[i][mid] > res: 
                res = mat[i][mid]
                largest_i = i 
        
        left, right = False, False
        if start>0 and mat[largest_i][mid]<mat[largest_i][mid-1]:
            left = True 

        if end < len(mat[0])-1 and mat[largest_i][mid]<mat[largest_i][mid+1]:
            right = True

        if not left and not right: 
            return [largest_i, mid] 

        if left: 
            end = mid - 1

        else: 
            start = mid + 1  

         


if __name__ == "__main__":
    print(findPeakGrid([
        [10,50,40,30,20],
        [1,500,2,3,4]]))



        
