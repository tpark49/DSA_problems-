def shortestDistanceColor(colors, queries):

    result = []

    #create dicitonary
    index_dict = {}
    for i, c in enumerate(colors): 
        if c in index_dict: 
            index_dict[c].append(i) 
        else: 
            index_dict[c] = [i] 

    print(index_dict)

    for query in queries:
        if query[1] in index_dict:
            #check if there is any after last index, if not just return first 
            if query[0]>index_dict[query[1]][-1]:
                result.append(abs(index_dict[query[1]][-1]- query[0]))
                continue
            #if it is smaller than biggest index in dictionary... 
            else:
                #start with the smallest index in dictionary
                i = 0
                while i < len(index_dict[query[1]]):
                    if index_dict[query[1]][i]>=query[0]:
                        result.append(abs(index_dict[query[1]][i]-query[0]))
                        break
                    i+=1
        #there is no number in dictionary so add -1 to list
        else:
            result.append(-1)
    return result

if __name__ == "__main__":
    print(shortestDistanceColor([1,2],[[0,3]]))
