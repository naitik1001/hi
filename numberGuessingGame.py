import random
print("number guessing game")
number = random.randint(1,9)
chances=0
print("guess a number between 1 to 9")
while chances  < 5:
    guess = int(input("enter your guess"))
    if guess == number:
        print("Congratulations You win the game!!!")
        break
    elif guess<number:
        print("Your guess was too low ,please try again",guess)
    else:
        print("your guess was too high,please try again",guess)
        chances+=1    
if not chances<5:
    print("You lose",number)
    