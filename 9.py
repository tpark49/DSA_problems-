def isPalindrome(x):
    res = 0 

    if x<0:
        return False 
    else: 
        
        temp = x
        while temp>0: 

            res = res*10 + temp%10 

            temp = temp //10 

    return res == x 