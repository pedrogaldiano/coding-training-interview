def jumpingOnClouds(c):

    clouds = [i for i,k in enumerate(c) if k == 0]
    print(clouds)
    for i in clouds:
        try:
            if i + 2 in clouds:
                clouds.remove(i+1)
        except:
            pass
    return len(clouds) - 1


x = [0, 0, 1, 0, 0, 1, 0]

print(jumpingOnClouds(x))
