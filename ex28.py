def max_3(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return "error"

print(max_3(23,500000,654661564651))
