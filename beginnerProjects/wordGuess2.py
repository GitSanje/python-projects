import  random
import  time
words = ["apple", "banana", "cat", "dog", "sun"]
word = random.choice(words)
guesses = ''
turns = 12

while turns > 0:

    fail = 0
    for w in word:
        if w in guesses:
            print(w,end='')
        else:
            print('_')
            fail += 1
  
    if fail ==0:
            print("you won the game")
            print("The word is: ", word)
            break


    guess = str(input("Guess a char: "))
    guesses += guess
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')
        if turns ==0:
            print("you loose")
            break










