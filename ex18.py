import random

def cow(x):
    res = 0
    counter = 0
    while counter<4:
        if num[counter]==x[counter]:
            res+=1
        counter+=1
    return res

def bull(y):
    res = 0
    for i in y:
        if i in num:
            res+=1
    return res


if __name__=="__main__":
    num = ""
    c = 0
    while c<4:
        num+=str(random.randint(1,9))
        c+=1    
    print(num)
    usr_inp = str(input("guess 4 digit number => "))
    print(str(cow(usr_inp))+" cows")
    print(str(bull(usr_inp)) +" bulls")

    
