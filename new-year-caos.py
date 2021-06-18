def minimumBribes(q):
    expected = [i for i in range(1, len(q)+1)]
    counter = {i: 0 for i in expected}
    
    while not q == expected:
        for i in range(len(q)-1):
            
            if q[i] > q[i+1]:
                temp  = q[i]
                q[i] = q[i+1]
                q[i+1] = temp

                counter[q[i+1]] += 1
                if counter[q[i+1]] > 2:
                    print('Too chaotic')
                    return
                    
    total = sum([i for i in counter.values()])
    print(total)


queue = [2, 5, 1, 3, 4]
minimumBribes(queue)