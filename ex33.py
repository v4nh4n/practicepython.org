dict_of_people = {
    "Albert": 1997,
    "Tom": 1993,
    "Emmy": 1998,
    "Brad": 1995
    }

print("Welcome to our birthday findouter! We know birthdays of: ")
for i in dict_of_people:
    print(i)
name = input("Whose birthday you want to find out? => ")
print(dict_of_people.get(name, "no such name"))
