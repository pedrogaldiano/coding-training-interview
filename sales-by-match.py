def sockMerchant(n, ar):
    ar = sorted(ar)
    dic = {}
    for i in ar:
        if i in dic:
            dic[i] =  dic[i] + 1
        else:
            dic[i] = 1

    print('\n', dic)
    pairs = 0
    for key in dic:
        temp = int(dic[key] / 2)

        if temp >= 1:
            pairs += temp

    return pairs

print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))


