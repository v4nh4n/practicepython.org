import random
def picker():
    with open("dictionary.txt", 'r') as f:
        line = f.readlines()
    return str(random.choice(line).strip())

def logic():
    print("Welcome to HANGMAN!")
    print("_ _ _ _ _ _ _ _ _")
    print("")
    
    show = []
    word = list(picker().lower())
    
    #creating lines for show
    for i in range(len(word)):
        show.append("_")
        
    guess_count = 6
    
    while guess_count>0:
        guess = input("Guess the letter => ")

        count_or_not=False
        c=0
        while c < len(word):
            if guess in word[c]:
                show[c] = guess
                count_or_not=True
            c+=1
            
        str_word = ""
        for i in show:
            str_word+=i+" "

        print("")
        print(str_word)
        print("")

        print(guess)
        print("")
        if count_or_not==False:
            guess_count-=1
        print("You have "+str(guess_count)+" guesses left")
        #print(word)
        #for winning
        if "_" not in show:
            print("You won!")
            break
        
logic()

