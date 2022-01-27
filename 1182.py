from cmath import inf


def shortestDistanceColor(colors, queries):
    color_map = {}
    for index, color in enumerate(colors):
        if color in color_map: 
            color_map[color].append(index)
        else: 
            color_map[color] = [index]


    def binary_search(color, target):
        if color not in color_map: 
            return -1
        color_index = color_map[color]

        l = 0 
        r = len(color_index)-1 

        while l<=r:
            mid = (l+r)//2

            if color_index[mid] == target: 
                return 0 

            elif color_index[mid]>target:
                r = mid - 1

            else: 
                l = mid + 1

        left_index, right_index = float("inf"), float("inf")

        if r>=0: 
            right_index = abs(color_index[r] - target)

        if l<len(color_index):
            left_index = abs(color_index[l] - target)
        
        return min(right_index, left_index, abs(color_index[mid]-target))

    result = [0] *len(queries)
    for i, (query_index, query_color) in enumerate(queries):
        if colors[query_index] != query_color:
            shortest_distance = binary_search(query_color, query_index)
            
            if shortest_distance == float("inf"):
                shortest_distance = -1

            result[i] = shortest_distance

    return result


if __name__ == "__main__":

    print(shortestDistanceColor([1,2],[[0,3]]))