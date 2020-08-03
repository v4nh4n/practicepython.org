a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
one_line = ""
for i in a:
    if i < 5:
        print(i)
        b.append(i)
        one_line += str(i)+" => "
print(b)
print(one_line)
        
