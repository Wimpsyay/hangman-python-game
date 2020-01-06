master = input("ik")
print("\n" * 50)
word = list(master)
length = len(word)
right = list("_" * length)
finished = False
while finished == False: #lange statement die checkt of je al gewonnen hebt
    guess = input('Noem een letter!')
    if guess not in master: #statement die checkt of je het woord goed raadt
        print("Helaas. Try again.")
    for letter in word:
        if letter == guess:
            index = word.index(guess)
            right[index] = guess
            word[index] = "_"
            print(right)
            if list(master) == right:
                print("Yeaaaah. Je hebt gewonnen.")
                again = input("Nog een keer? y/n ")
                if again == "y": #if else statement die checkt of iemand nog een keer wilt spelen
                    master = input("Kies het volgende woord:")
                    print("\n" * 50)
                    word = list(master)
                    length = len(word)
                    right = list("_" * length)
                else:
                    finished = True