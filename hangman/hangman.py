import random, time, list_v, man

word = random.choice(list_v.list_v).casefold()

def menu():
    print(man.logo)
    print("Guess this word - ",end = "")
    for i in range(len(word)):
        print("_",end='')
        time.sleep(0.5)

def display(underscores,count):
    for i in range(len(underscores)): print(underscores[i],end='')
    print(man.hangman[6 - max(count,0)])
    print(f"\nLIFE'S = {count}/6\n{'-'*40}")

def decide(underscore_word,count):
    if underscore_word == list(word):
        print("\nYou won the game")
        exit()
    elif count < 1:
        print(f"\nYou lost the game\n\t\tThe secret word was [{word}]")
        exit()

def take_input():
    underscore_word = []
    underscore_word += '_'*len(word)
    count = 6
    while True:
        decide(underscore_word, count)
        letter = input("\nEnter a letter : ").casefold().strip()
        if not letter.isalpha() :
            print(f"{letter} is Invalid Character Try again please")
            continue
        elif len(letter) > 1:
            print(f"{letter} invalid Only single letter is allowed")
            continue
        elif letter in underscore_word :
            print(f"{letter} is already Guessed")
            display(underscore_word,count)
            continue
        elif letter not in word:
            count -= 1
            print(f"{letter} - Sorry Wrong Guess, you will loose a life")
            display(underscore_word,count)
            continue
        for i in range(len(word)):
            if letter == word[i]: underscore_word[i] = word[i]
        display(underscore_word, count)

def main() :
    print(word)
    menu()
    take_input()
if __name__ == "__main__": main()