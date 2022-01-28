def minAvailableDuration(slots1, slots2, duration):

    i, j = 0 , 0

    slots1 = sorted(slots1, key=lambda x: x[0])
    slots2 = sorted(slots2, key=lambda x: x[0])

    while i<len(slots1) and j<len(slots2): 
        
        starting = max(slots1[i][0], slots2[j][0])
        ending = min(slots1[i][1], slots2[j][1])

        if ending - starting >= duration: 
            return [starting, starting +duration]

        
        if slots2[j][1]>slots1[i][1]:
            i+=1
        else:
            j+=1

if __name__ == "__main__":
    print(minAvailableDuration(
        [[10,60]],
        [[12,17],[21,50]],
        8
    ))

            
