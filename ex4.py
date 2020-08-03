number = int(input("ENTER ANY NUMBER => "))
res = []
x = range(1, number+1)
for i in x:
    if number%i==0:
        res.append(i)

print(res)
