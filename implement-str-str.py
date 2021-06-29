def mine():
    haystack = "caramelo azul num fusca goiano ai meu deuxx como é bom comer miojo, nem é aaaaa teste de string é um saco..."
    needle = "jo"
    if needle == '':
        return 0

    elif needle in haystack:
        return haystack.index(needle)

    return -1

# Better than mine, AGAIN ;-; hahahaha
def other():
    haystack = "caramelo azul num fusca goiano ai meu deuxx como é bom comer miojo, nem é aaaaa teste de string é um saco..."
    needle = "jo"
    if needle == '':
        return 0
    return haystack.find(needle)


import timeit

print('mine:  ', timeit.timeit(mine, number=100000000))
print('other:  ', timeit.timeit(other, number=100000000))

