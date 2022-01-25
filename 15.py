def threeSum(num):
    num = sorted(num)
    res = []
    for i in range(len(num)):
        if i>0 and num[i] == num[i-1]:
            continue 
            
        l = i + 1
        r = len(num)-1

        while l<r:
            if num[i] + num[l] + num[r] == 0: 
                res.append([num[i], num[l], num[r]])
                l+=1
                while num[l]==num[l-1] and l<len(num):
                    l+=1
            
                r-=1
                while num[r]==num[r+1] and r>=0:
                    r-=1
            elif num[i] + num[l] + num[r] > 0:
                r-=1
                while num[r]==num[r+1] and r>=0: 
                    r-=1
            else: 
                l+=1
                while num[l]==num[l-1] and l<len(num):
                    l+=1
    return res
        
                
            

if __name__ == "__main__":
    print(threeSum([0]))

