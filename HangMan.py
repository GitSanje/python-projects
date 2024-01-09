import  random
print('*'*50)
print("Welcome to the Hangman Game")
print('*'*50)

fruits = [
    "apple", "orange", "banana", "grape", "strawberry", "blueberry",
    "kiwi", "watermelon", "pineapple", "mango", "pear", "peach", "plum",
    "cherry", "lemon", "lime", "avocado", "pomegranate", "raspberry",
    "blackberry", "cantaloupe", "fig", "guava", "passion fruit",
    "dragon fruit", "kiwifruit", "nectarine", "papaya", "apricot",
    "cranberry", "grapefruit", "honeydew", "tangerine"
]
hangman = '''
      ___
     |   |
     |   o
     |  /|\\
     |  / \\
     |
    _|_
'''


lstHangman = list(hangman)
word =random.choice(fruits)

VerticalIdx = [index for index,char in enumerate(hangman) if char == '|']
horizontalIdx = [index for index,char in enumerate(hangman) if char == '_']
leftIdx = [index for index,char in enumerate(hangman) if char == '/']
rightIdx = [index for index,char in enumerate(hangman) if char == '\\']
headIdx = hangman.index('o')
manIdx = [ headIdx,leftIdx[0],VerticalIdx[4], rightIdx[0], leftIdx[1],rightIdx[1]]
hangIdx =VerticalIdx[1]
HangmanWord = lstHangman[:]


# for idx in manIdx:
#
#     HangmanWord[idx] = ' '
# HangmanWord = ''.join(HangmanWord)
# HangmanWord= ''.join([' ' if idx in manIdx else char for idx,char in enumerate(HangmanWord)])
# print(HangmanWord )
# print(manIdx)

# Returns the list that is differ from original list(hangman) , contains remaining chars after removing
# the chars equal to the len of word

def HangManRemainingList(word,HangmanWord):

    if len(word) <= 6:

        idxs= manIdx[-1:-len(word)-1:-1]
        HangmanWord = ''.join([' ' if idx in idxs else char for idx, char in enumerate(HangmanWord)])
        idxs =idxs[::-1]
        return idxs, HangmanWord
    else:
        WordIndx = manIdx[:]
        remIndx = len(word) -7

        WordIndx += [' ']* (remIndx+1)
        WordIndx[6] = hangIdx
        if remIndx ==0:
            HangmanWord = ''.join([' ' if idx in WordIndx else char for idx, char in enumerate(HangmanWord)])
        elif remIndx >0:
            c=0
            for i in range(remIndx):
                if i < 3:
                    WordIndx[7+i] = horizontalIdx[i]
                else:
                    if remIndx ==4 and remIndx == 7:
                        continue
                    WordIndx[7+i] =VerticalIdx[c]
                    c+=1
            HangmanWord = ''.join([' ' if idx in WordIndx else char for idx, char in enumerate(HangmanWord)])
            part_to_move = WordIndx[10:]
            WordIndx = WordIndx[7:10]+[20]+WordIndx[:6]
            #
            WordIndx = part_to_move+ WordIndx


        return WordIndx, HangmanWord


charIndeces, RemainingList = HangManRemainingList(word,HangmanWord)
print(charIndeces)
print(RemainingList)
print("THe word is fruit name\n")
print("The lenght of word is ", len(word))
strings = ''
OutputWOrd = '_'* len(word)
count = 0
turns = len(word)+3

while turns > 0:

    Guess = str(input("Enter a letter: "))
    if Guess not in word:
        i = charIndeces[count]
        char = HangmanWord[i]
        RemainingList = RemainingList[:i] + char + RemainingList[i + 1:]
        print(RemainingList)
       # print("You have ", turns, "remaining ")
        count+=1
        turns -=1
        print(OutputWOrd)
        if turns == 0 or count>=len(charIndeces) :
            print("You loose the game. Play next time good luck ")
            print("The word is ", word)
            break

    else:

        indecesChar = [ix for ix, char in enumerate(word) if char == Guess]

        if len(indecesChar) > 1:

            for idx in indecesChar:
                OutputWOrd = OutputWOrd[:idx] + Guess + OutputWOrd[idx + 1:]
        else:
            idx=indecesChar[0]
            OutputWOrd = OutputWOrd[:idx] + Guess + OutputWOrd[idx + 1:]

        if '_' not in OutputWOrd:
            print("Congratulation!, You have won the game in ",turns,"turns")
            break
        print(RemainingList)
        print(OutputWOrd)



# original = ''.join(lstHangman)
# print(original)
# print(original.index('o'))
# print(original.index('/'))
# print(original.rindex('/'))
# print(original.index('\\'))
# print(original.rindex('\\'))
# print(original.rindex('|'))


