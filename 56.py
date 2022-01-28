def merge(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    result = [sorted_intervals[0]]

    for i in range(1, len(sorted_intervals)): 
        
        #merge requirements
        if sorted_intervals[i][0] <= result[-1][1]: 
            result[-1][1] = max(sorted_intervals[i][1], result[-1][1])

        else: 
            result.append(sorted_intervals[i])
    
    return result


if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))