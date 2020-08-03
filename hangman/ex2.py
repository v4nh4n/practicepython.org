print("Welcome to HANGMAN!")
print("_ _ _ _ _ _ _ _ _")
print("")
show = list("_________")
word = list("EVAPORATE")
counter=0
while "_" in show:
    guess = input("Guess the letter => ")

    c=0
    while c < len(word):
        if guess in word[c]:
            show[c] = guess
        c+=1
        
    str_word = ""
    for i in show:
        str_word+=i+" "

    print("")
    print(str_word)
    print("")
        

