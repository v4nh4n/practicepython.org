res = {}
with open("C:\\Users\\v4h4\\Desktop\\text.txt", "r") as t:
    line = t.readline()
    while line:
        line = line.strip()
        if line in res:
            res[line]+=1
        else:
            res[line]=1
        line = t.readline()
print(res)



