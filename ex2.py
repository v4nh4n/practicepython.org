number = int(input("ENTER A NUMBER => "))
if number%4==0:
    print("MULTIPLE OF 4")
elif number%2==0:
    print("EVEN")
else:
    print("ODD")
num = int(input("ENTER NUM1 => "))
check = int(input("ENTER ANOTHER NUM TO DIVIDE => "))
res = num/check
if res%2==0:
    print("YOUR RESULT IS "+str(int(res))+" IS EVEN")
else:
    print("YOUR RESULT IS "+str(int(res))+" IS ODD")
    
