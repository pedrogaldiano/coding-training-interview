def countingValleys(steps, path):
    valleys = 0
    relative_to_sea = 0

    for i in range(steps):
        if path[i] == 'D':
            relative_to_sea -= 1
        elif path[i] == 'U':
            relative_to_sea += 1

        if relative_to_sea == 0 and path[i] == 'U':
            valleys += 1
    return valleys
    
print(countingValleys(8, 'UDDDUDUU'))