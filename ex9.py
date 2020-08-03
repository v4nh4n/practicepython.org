import random
guess_num = 0
while True:

    a = random.randint(1,9)

    while True:
        b = int(input("GUESS FROM 1-9! => "))
        if b==a:
            print("EXACTLY RIGHT!")
            guess_num+=1
            break
        elif b<a:
            print("too low")
            guess_num+=1
        elif b>a:
            print("too high")
            guess_num+=1

    q = input("EXIT? y/n")
    if q=="y":
        break

    

print(guess_num)
