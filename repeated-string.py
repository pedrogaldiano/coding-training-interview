def repeatedString(s, n):
    if s == 'a':
        return n
    else:
        letters = len(s)
        counter = s.count('a')
        x = n // letters

        modded = n % letters
        if modded > 0:
            y = s[:modded].count('a')
            return (counter * x) + y

        return (counter * x)
        


x = 'jdiacikk'
n = 899491

print(repeatedString(x,n))