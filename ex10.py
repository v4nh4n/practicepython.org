import random

a = random.sample(range(1,100),12)
b = random.sample(range(1,100),12)

res_overlaps = [x for x in set(a) if x in b] 
res = []

for element in res_overlaps:
    if element not in res:
        res.append(element)

print(res)
