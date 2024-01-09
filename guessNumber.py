import random
import math
print("Welcome to the Guessing Game\n")
print('*'*20)
print("Rule: You provide the range")
print("I will generate random number in that range. ")

print("Enter the range \n")

A = int(input("Enter start number: "))
B = int(input("Enter end number: "))

if ( A < 0 or B<0):
    print("Numbers can't be negative")

    
elif( A > B):
    print("Start number can't be greater than end")
    


def GuessNumber(A,B):
    chances = round(math.log(B-A +1,2))
    print("You have", chances,"chances to guess")
    
    
    chancesleft=chances
    
    count =0
    
    randN = random.randint(A,B)
    while count< chances:
        C= int(input("Enter your guess: "))
        count+=1
        chancesleft-=1
        if(C==randN):
            print("Congrats you got it")
            print("You have guess in ", count, "time")
            break
        
        elif(C> randN):
            
            print("High\n")
            print("Try again!")
            
            print("You have ",chancesleft," chances left\n")
        elif (C<randN):
          
            print("Low\n")
            print("Try again!")
            print("You have ",chancesleft," chances left\n")
            
    if(count >= chances):
        print("Game over !")
        print("The number is"+randN)
        
        
        
GuessNumber(A,B) 
    
    
