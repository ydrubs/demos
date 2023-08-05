import random

wordBank = ["thrown","tonight","plane","hundred","porch","cloud","eat","wooden","fierce","scale",
"morning","younger","joy","tone","tent","wait","buffalo","written","cent","avoid",
"serious","got","shop","win","white","fish","light","do","nearly","officer",
"determine","west","duty","level","worry","after","score","verb","parts","region"
"money","walk","give","rose","history","do","turn","storm","heat","numeral"]


def choose_word():
    chosenWord = random.choice(wordBank)  # Choose a word from the bank
    return chosenWord

def scrambleWord(chosenWord):
    wordList = []
    scrambledWord = ""
    #print(chosenWord)
    for i,v in enumerate(chosenWord): #Break word up into letters
        wordList.append((v))
    #print(wordList)
    random.shuffle(wordList) #shuffle letters in the word
    #print(wordList)
    scrambledWord = scrambledWord.join(wordList) #combine scrambled letters from word and return
    #print(wordList)
    return scrambledWord

def newWord():
    myWord = choose_word()
    scrambledWord = scrambleWord(myWord)
    return myWord, scrambledWord

def run():
    score = 0

    while True:
        rescrambles_word = ""
        currentRound = 1
        if currentRound == 1:
            getWord = newWord()
            print("Score: " + str(score))
            print(getWord[1])
            currentRound = 0

        if currentRound == 0:
            guess = input("Unscramble the word or press '1' to re-arrange the letters: ")
            if guess.casefold() == getWord[0]:
                print("correct!\n")
                score = score + 1
                currentRound = 1

            while guess.casefold() != getWord[0]:
                if guess == '1':
                    rescrambles_word = scrambleWord(getWord[0])
                    print("\n")
                    print(rescrambles_word)
                    guess = input("Unscramble the word or press '1' to re-arrange the letters: ")


                print("try again\n")
                print(getWord[1])
                guess = input("Unscramble the word or press '1' to re-arrange the letters: ")

                if guess.casefold() == getWord[0]:
                    print("correct!\n")
                    score = score + 1
                    currentRound = 1
                    break


run()