def guesser():
    i = 0
    m = 100
    mid = 50

    print("Guess some number btw 0-100")
    condition=input("Is your guess"+str(mid)+"? exact/low/high")
    while condition!="exact":
        if condition=="low":
            i = mid + 1
        elif condition=="high":
            m = mid - 1

        mid = (i+m)//2
        condition=input("Is your guess"+str(mid)+"? exact/low/high")
    return "I did it !!!!"

print(guesser())



