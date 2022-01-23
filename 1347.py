def minSteps(s, t): 
    count_dict = {}
    count_t = 0
    for i in s: 
        if i in count_dict:
            count_dict[i] += 1
        else: 
            count_dict[i] = 1
    
    for j in t: 
        if j in count_dict: 
            if count_dict[j] == 0: 
                count_t +=1 
            else: 
                count_dict[j]-=1
        else: 
            count_t +=1 
        
    return count_t


if __name__ == "__main__":
    s = "anagram"
    t = "mangaar"
    print(minSteps(s, t))