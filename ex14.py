def minus_duplicate(a):
    if type(a)==list:
        x = set(a)
        t = []
        for i in x:
            t.append(i)
        return t
    else:
        return "this is not a list"
    
def minus_duplicate_loop(a):
    if type(a)==list:
        q = []
        for i in a:
            if i not in q:
                q.append(i)
        return q
    else:
        return "this is not a list"

y = minus_duplicate([1, 5, 4, 8, 9, 5, 6, 3, 1, 5, 4, 8, 4, 5, 5, 5, 5, 5])
print(y)
x = minus_duplicate_loop([1, 5, 4, 8, 9, 5, 6, 3, 1, 5, 4, 8, 4, 5, 5, 5, 5, 5])
print(x)
