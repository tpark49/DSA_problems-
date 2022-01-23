

def groupAnagram(strs):
    
    answer = {}
    
    for string in strs: 
        if "".join(sorted(string)) in answer:
            answer["".join(sorted(string))].append(string)
        else: 
            answer["".join(sorted(string))] = [string]
    return list(answer.values())


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagram(strs))