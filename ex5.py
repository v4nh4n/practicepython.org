import random

a = random.sample(range(1,100),10)
b = random.sample(range(1,100),10)
c = []
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
        
print(a)
print(b)
print(c)
        
