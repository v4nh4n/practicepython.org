table = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def placement(x, y, z):
    table[x][y] = z

a_wins = False
b_wins = False

print("   0  1  2")
ye=0#for side numbs
for i in table:#show table     
        print(str(ye)+" "+str(i))
        ye+=1
        
while not (a_wins==True or b_wins==True):
    a_row = int(input("plA => row: "))
    a_column = int(input("plA => column: "))
    b_row = int(input("plB => row: "))
    b_column = int(input("plB => column: "))

    placement(a_row, a_column, 1)
    placement(b_row, b_column, 2)
            
    if a_wins==False:  # iterate thorugh rows and columns and find if a_wins is True
        c = 0
        a = 0
        a_count = 0
        while c<3:
            while a<3:
                if 1==table[c][a]:
                    a_count+=1
                else:
                    a_count=0
                a+=1
            if a_count==3:
                a_wins=True
                break
            a_count=0
            a=0
            c+=1
        c=0
        while c<3:
            while a<3:
                if 1==table[a][c]:
                    a_count+=1
                else:
                    a_count=0
                a+=1
            if a_count==3:
                a_wins=True
                break
            a_count=0
            a=0
            c+=1
        if table[0][0]==1 and table[1][1]==1 and table[2][2]==1:
            a_wins = True
        if table[0][2]==1 and table[1][1]==1 and table[2][0]==1:
            a_wins = True
            
    if b_wins==False:  #same thing with b
        c = 0
        a = 0
        a_count = 0
        while c<3:
            while a<3:
                if 2==table[c][a]:
                    a_count+=1
                else:
                    a_count=0
                a+=1
            if a_count==3:
                b_wins=True
                break
            a_count=0
            a=0
            c+=1
        c=0
        while c<3:
            while a<3:
                if 2==table[a][c]:
                    a_count+=1
                else:
                    a_count=0
                a+=1
            if a_count==3:
                b_wins=True
                break
            a_count=0
            a=0
            c+=1
        if table[0][0]==2 and table[1][1]==2 and table[2][2]==2:
            b_wins = True
        if table[0][2]==2 and table[1][1]==2 and table[2][0]==2:
            b_wins = True

        
    print("   0  1  2")
    ye=0    #for side numbs
    for i in table:     #show table     
        print(str(ye)+" "+str(i))
        ye+=1

if a_wins==True:
    print("Player A wins")
if b_wins==True:
    print("Player B wins")

