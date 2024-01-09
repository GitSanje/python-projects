import random

print('*'*30)
print("Welcome to the mastermind game.")
print('*'*30)

def win(trials):
    print("\nCongratulation! You won the game.,Now you have become master mind")
    print(f"You have won in {trials} trails")
    exit(0)

def validate(intputValue,length):
    if intputValue.isdigit() and len(intputValue) == length:
        return True
    else:
        return False

random.seed(5)
digits = str(random.randint(1100,9999))
length = len(digits)
guessed = ['X']*length
print("\nYou are the player two")
print("\nI am the player one")
print(f"\nThe hidden digit has  length {length}")



while True:
    Guess = input("Guess the digit: ")

    if Guess == digits:
        print("Great! You guessed the number in just 1 try! You're a Mastermind!")
        exit(0)
    if(validate(Guess,length)):
        trials = 0

        while True:
            count = 0
            rightGuess = ''
            Guess = input("Enter your next choice of numbers: ")
            if (validate(Guess, length)):
                number = str(Guess)
                for i, (ch1,ch2 ) in enumerate(zip(digits,number)):
                        if ch1==ch2:
                            guessed[i] = ch1
                            count += 1
                            rightGuess += ch1

                trials += 1
                value = ''.join(guessed)
                print(value,digits)
                if value== digits:
                        win(trials)
                else:
                        print(' '.join(guessed))
                        print(f'You have guess {count} digits right: {rightGuess}')



            else:
                print(f"Please enter a {length}-digit number.")
    else:
       print(f"Please enter a {length}-digit number.")






