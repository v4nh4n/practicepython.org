a = [5, 15, 20, 30]

def make_list(x):
    new_list = []
    if type(x) is list:
        for i in range(x[0], x[-1]+1):
            new_list.append(i)
        return new_list
    else:
        return "It's not a list"

    
print(make_list(a))
