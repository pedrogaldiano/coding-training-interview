def minimumSwaps(arr):
    length = len(arr)
    counter = 0

    hash = {i:k for i,k in zip(range(1, length+1),arr)}
    print(hash)
    for i in range(1, length+1):
        # The position 1 has 1? The position 2 has 2? And so on...
        if hash[i] != i:
            temp = hash[i]
            hash[i] = hash[i+1]
            hash[i+1] = temp
            counter += 1

    print(hash)
    return counter

z = [1, 3, 5, 2, 4, 6, 7]
y = [2, 3, 4, 1, 5]
x = [4,3,1,2]
print(minimumSwaps(y))
