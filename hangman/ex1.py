import random
def picker():
    with open("dictionary.txt", 'r') as f:
        line = f.readlines()
    print(random.choice(line).strip())

picker()
