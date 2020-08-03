def backwards_text(a):
    x = a.split()
    y = []
    c1 = 0
    c2 = len(x)-1
    while c2>=c1:
        y.append(x[c2])
        c2-=1
    res = ""
    for i in y:
        res+=i+" "
    return res

x = str(input("Type a sentence... "))
print(backwards_text(x))

    
