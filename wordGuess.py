
import  random
import  time
print("*"*50)
print("Welcome to word guessing game")
print("*"*50)


def timeCheck(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        print("You have taken {:.2f} seconds".format(time.time() - start))
    return  wrapper
name = str(input("Enter your name : "))


word_list = ["apple", "banana", "cat", "dog", "sun"]

@timeCheck
def GuessWord():
    randStr = random.choice(word_list)
    lenRanStr = len(randStr)
    strings = list(' _ ' * lenRanStr)
    modifiedStr = [w for w in strings if ' ' not in w]
    turns = lenRanStr * 2
    while turns>0:
        guessChr = str(input("Guess a alphabet: "))
        if guessChr in randStr:


                allIndeces = [index for index, char in enumerate(randStr) if char == guessChr]
                if len(allIndeces) == 1:
                    modifiedStr[allIndeces[0]] = guessChr
                    ShowStr = ' '.join(modifiedStr)


                elif len(allIndeces) > 1 :
                    for i in allIndeces:
                        if modifiedStr[i] == '_':
                            modifiedStr[i] = guessChr
                            ShowStr = ' '.join(modifiedStr)
                print(ShowStr)
                if not '_' in modifiedStr:
                    print("Congratulation! you have guessed the word")
                    break
        else:
            turns -= 1
            print("You have ",turns,"turns left")


GuessWord()











# # Iterate over a copy of the list to avoid modification during iteration
# for w in strings[:]:
#     if ' ' in w:
#         strings.remove(w)