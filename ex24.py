rows = int(input("Enter a number of rows = > "))
columns = int(input("Enter a number of columns = > "))

def draw_table(r, c):
    for i in range(c):
        print(r*" --- ")
        print(int(r+1) * "|    ")
    print(r*" --- ")
draw_table(rows, columns)
