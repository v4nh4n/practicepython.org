while True:
    a = input("PLAYER A RSP => ")
    b = input("PLAYER B RSP => ")

    if a=="r" and b=="s":
        print("A wins")
        break
    elif a=="s" and b=="p":
        print("A wins")
        break
    elif a=="p" and b=="r":
        print("A wins")
        break
    elif a=="s" and b=="r":
        print("B wins")
        break
    elif a=="p" and b=="s":
        print("B wins")
        break
    elif a=="r" and b=="p":
        print("B wins")
        break
    elif a==b:
        print("EVEN 1 MORE TIME")
        
