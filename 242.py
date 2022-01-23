from collections import Counter

def isAnagram(s, t):
    s_dict = Counter(s)
    
    for i in t: 
        if i in s_dict: 
            s_dict[i]-=1
        else: 
            return False 

    for i in list(s_dict.values()):
        if i != 0: 
            return False 

    return True  


if __name__ == "__main__":
    s = "aacc"
    t = "ccac"
    print(isAnagram(s, t))