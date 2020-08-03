name = input("GIVE ME YOUR NAME=> ")
age = int(input("GIVE ME YOUR AGE=> "))
current_year = 2020
years_left = current_year - age
copy =("OK "+name+" YOU WILL TURN 100 in "+str((current_year + years_left))+"\n")
print(copy)
number = int(input("How many copies of that you want to see? => "))
print(number*copy)
