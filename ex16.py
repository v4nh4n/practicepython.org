import random
import string

def pass_generator(length):
    x = string.ascii_letters
    res = ""
    l = int(length/2)
    for i in range(l):
        res+=random.choice(x)
        res+=str(random.randint(1,9))
    return res

ext = False

while ext==False:
    inp = int(input("To generate password define the length of password => "))
    print(pass_generator(inp))
    ex = str(input("another one? => y/n "))
    if ex=="n":
        ext=True
        
