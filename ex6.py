a = input("ENTER A STRING: ")
x = int((len(a)/2))
print(x)
h1 = a[:x]
h2 = a[x+1:]
print(h1)
print(h2)
if h1==h2:
    print("palindrome!")
else:
    print('not a palindrome...')
