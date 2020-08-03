def prime_number(num):
    if num==1 or num==2:
        return True
    for i in range(num):
        if i>1 and num%i==0:
            return False
    return True

while True:
    number = int(input("ENTER A NUMBER (CTRL+C TO EXIT) => "))
    print(prime_number(number))
