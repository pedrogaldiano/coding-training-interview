def hourglassSum(arr):
    values = []
    for r in range(1,5):
        for c in range(1,5):
            
            elements = [
                arr[r-1][c-1], arr[r-1][c], arr[r-1][c+1]
                             , arr[r][c],
                arr[r+1][c-1], arr[r+1][c], arr[r+1][c+1]]
            
            values.append(sum(elements))

    return max(values)
            

    

x = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]]

print(hourglassSum(x))