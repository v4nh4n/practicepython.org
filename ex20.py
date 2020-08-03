##q = list(input("Write a list in [] => "))
##a = q.sort()
##b = input("Write a number => "  )
##
##
##def find_el(x):
##    for i in x:
##        if i==b:
##            return True
##    return False

def binary_search(x, y):
    if len(x)==0 or (len(x)==1 and x[0]!=y):
        return False

    mid = x[len(x)//2]
    if y==mid:
        return True
    if y<mid:
        return binary_search(x[:len(x)//2],y)
    if y>mid:
        return binary_search(x[(len(x)//2+1):],y)

a = [1,5,6,9,8,5]
print(binary_search(a, 5))
