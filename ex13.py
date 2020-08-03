def fibonacci_num(x):
    res = [1,1]

    if x==1:
        return [1]
    elif x==2:
        return res

    c = 1
    while c<x-1:
        res.append(res[c]+res[c-1])       
        c+=1
    return res

print(fibonacci_num(3))          
    
