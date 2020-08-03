prime = []
with open("C:\\Users\\v4h4\\Desktop\\prime.txt") as p:
    line = p.readline()
    while line:
        prime.append(int(line))
        line = p.readline()

happy = []
with open("C:\\Users\\v4h4\\Desktop\\happy.txt") as h:
    line = h.readline()
    while line:
        happy.append(int(line))
        line = h.readline()

overlap = []
for i in prime:
    if i in happy:
        overlap.append(i)

print(overlap)
